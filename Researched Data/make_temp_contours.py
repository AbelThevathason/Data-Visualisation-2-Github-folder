"""
Builds filled contour bands (isobands) of maximum temperature as GeoJSON.

Run this from the folder that holds your HTML page:
    python make_temp_contours.py

Needs: pip install numpy pandas scipy matplotlib shapely
(matplotlib 3.8 or newer)
"""
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from scipy.ndimage import binary_fill_holes, gaussian_filter
from scipy.spatial import cKDTree
from shapely.geometry import MultiPolygon, Polygon, mapping
from shapely.geometry.polygon import orient

CSV_PATH = "Researched Data/Processed Data/australia_max_temp_2024.csv"
OUT_PATH = "Researched Data/Processed Data/australia_max_temp_bands_2024.geojson"

LEVELS = [18, 22, 26, 30, 34]   # band edges in degrees C
FLOOR = 0                        # lower limit for the first band
CEILING = 100                    # upper limit for the last band
GRID_STEP = 0.2                  # output grid spacing in degrees
MASK_FACTOR = 2.5                # grid cells further than this many typical point gaps from any data point are left empty
SMOOTH_SIGMA = 1.0               # set to 0 for no smoothing


def smooth_keep_mask(z, sigma):
    """Gaussian smooth without bleeding values into missing cells."""
    if sigma <= 0:
        return z
    valid = ~np.isnan(z)
    num = gaussian_filter(np.where(valid, z, 0.0), sigma)
    den = gaussian_filter(valid.astype(float), sigma)
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    return np.where(valid, out, np.nan)


def rings_to_geometry(rings):
    """Combine rings with the even odd rule so holes are handled."""
    geom = None
    for ring in rings:
        if len(ring) < 4:
            continue
        poly = Polygon(ring).buffer(0)
        geom = poly if geom is None else geom.symmetric_difference(poly)
    return geom


def orient_for_d3(geom):
    """d3 geo (used by Vega) wants exterior rings clockwise and holes anticlockwise.
    This is the opposite of the GeoJSON standard, and wrong winding fills the whole map."""
    if isinstance(geom, Polygon):
        return orient(geom, sign=-1.0)
    if isinstance(geom, MultiPolygon):
        return MultiPolygon([orient(p, sign=-1.0) for p in geom.geoms])
    return geom


def band_label(lower, upper):
    if lower == FLOOR:
        return "below " + str(upper)
    if upper == CEILING:
        return str(lower) + " and above"
    return str(lower) + " to " + str(upper)


df = pd.read_csv(CSV_PATH)
df = df[df["max_temp"] > 0].copy()

# The CSV is a scattered set of points, so interpolate onto a regular grid first
points = df[["lon", "lat"]].to_numpy()
values = df["max_temp"].to_numpy()

lons = np.arange(df["lon"].min(), df["lon"].max() + GRID_STEP, GRID_STEP)
lats = np.arange(df["lat"].min(), df["lat"].max() + GRID_STEP, GRID_STEP)
grid_lon, grid_lat = np.meshgrid(lons, lats)
grid_points = np.column_stack([grid_lon.ravel(), grid_lat.ravel()])

z = griddata(points, values, grid_points, method="linear").reshape(grid_lon.shape)

# Leave cells empty where there is no nearby data (ocean and gaps between islands)
tree = cKDTree(points)
typical_gap = np.median(tree.query(points, k=2)[0][:, 1])
nearest, _ = tree.query(grid_points)
has_data = (nearest <= MASK_FACTOR * typical_gap).reshape(z.shape)
# Fully enclosed gaps inside the continent are missing data, not sea, so fill them
has_data = binary_fill_holes(has_data)
z[~has_data] = np.nan

z = smooth_keep_mask(z, SMOOTH_SIGMA)

edges = [FLOOR] + LEVELS + [CEILING]
cs = plt.contourf(lons, lats, np.ma.masked_invalid(z), levels=edges)

features = []
for i, path in enumerate(cs.get_paths()):
    geom = rings_to_geometry(path.to_polygons())
    if geom is None or geom.is_empty:
        continue
    geom = orient_for_d3(geom)
    lower, upper = edges[i], edges[i + 1]
    features.append({
        "type": "Feature",
        "properties": {"level": lower, "upper": upper, "label": band_label(lower, upper)},
        "geometry": mapping(geom),
    })

with open(OUT_PATH, "w") as f:
    json.dump({"type": "FeatureCollection", "features": features}, f)

print("Wrote", len(features), "bands to", OUT_PATH)
