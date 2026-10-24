import xarray as xr
import pandas as pd

# 1. Load the SILO NetCDF file
ds = xr.open_dataset('Researched Data/Raw Data/2024.monthly_rain.nc')

# 2. Sum the 12 monthly slices into an annual total
annual_total = ds['monthly_rain'].sum(dim='time')

# 3. Convert to a DataFrame and drop missing/ocean points
df = annual_total.to_dataframe().reset_index().dropna()

# Subsample every 45th point (reduces 1MB file down to ~130KB)
df_sampled = df.iloc[::45].copy()

# 5. Rename column for clarity
df_sampled.rename(columns={'monthly_rain': 'annual_rainfall_mm'}, inplace=True)

# 6. Save to CSV inside your project data folder
df_sampled.to_csv('Researched Data/Processed Data/silo_annual_rainfall_2024.csv', index=False)
print("Saved silo_annual_rainfall_2024.csv successfully!")