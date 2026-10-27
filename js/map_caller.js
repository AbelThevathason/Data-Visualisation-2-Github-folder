// JavaScript file orchestrating Vega/Vega-Lite chart rendering in sequential order
const embedOpt = { "actions": false };

// ==========================================
// SECTION 1: Land Allocation & Footprint
// ==========================================

// Chart 1: Spatial Land Use Map
vegaEmbed('#map-container-land-use', 'js/map_land_use.json', embedOpt)
  .then(result => console.log("Chart 1 (Land Use Map) rendered."))
  .catch(console.error);

// Chart 2: Land Use Breakdown Treemap
vegaEmbed('#map-container-treemap', 'js/treemap_spec.json', embedOpt)
  .then(result => console.log("Chart 2 (Treemap) rendered."))
  .catch(console.error);

// Chart 3: Land Tenure vs Land Use Flow (Sankey Diagram)
vegaEmbed('#chart-container-sankey', 'js/sankey.json', embedOpt)
  .then(result => console.log("Chart 3 (Sankey Diagram) rendered."))
  .catch(console.error);

// ==========================================
// SECTION 2: Spatial & Historical Climate Pressures
// ==========================================

// Chart 4: Annual Rainfall Distribution (Binned Map)
vegaEmbed('#map-container-rainfall', 'js/map_rainfall.json', embedOpt)
  .then(result => console.log("Chart 4 (Rainfall Map) rendered."))
  .catch(console.error);

// Chart 5: Maximum Temperature Distribution (Binned Heatmap)
vegaEmbed('#map-container-max-temp', 'js/map_max_temp.json', embedOpt)
  .then(result => console.log("Chart 5 (Max Temp Map) rendered."))
  .catch(console.error);

// Chart 6: 25-Year Historical Rainfall Matrix Heatmap
vegaEmbed('#chart-container-heatmap', 'js/heatmap_rainfall_matrix.json', embedOpt)
  .then(result => console.log("Chart 6 (Matrix Heatmap) rendered."))
  .catch(console.error);

// ==========================================
// SECTION 3: Economic Impacts of Climate Shocks
// ==========================================

// Chart 7: Grain Industry Rate of Return Map
vegaEmbed('#chart-container-grains-diverging', 'js/diverging_grains_chart.json', embedOpt)
  .then(result => console.log("Chart 7 (Grains Map) rendered."))
  .catch(console.error);

// Chart 8: Beef Industry Rate of Return Map
vegaEmbed('#chart-container-beef-diverging', 'js/diverging_beef_chart.json', embedOpt)
  .then(result => console.log("Chart 8 (Beef Map) rendered."))
  .catch(console.error);

// Chart 9: Farm Profit Trends Line Chart (2000–2024)
vegaEmbed('#chart-container-linechart', 'js/line_chart.json', embedOpt)
  .then(result => console.log("Chart 9 (Profit Line Chart) rendered."))
  .catch(console.error);

// Chart 10a: Beef Sector Dual-Axis (Rainfall vs. Farm Profit)
vegaEmbed('#chart-container-beef-dual', 'js/chart_beef_dual_axis.json', embedOpt)
  .then(result => console.log("Chart 10a (Beef Dual Axis Chart) rendered."))
  .catch(console.error);

// Chart 10b: Grains Sector Dual-Axis (Rainfall vs. Farm Profit)
vegaEmbed('#chart-container-grains-dual', 'js/chart_grains_dual_axis.json', embedOpt)
  .then(result => console.log("Chart 10b (Grains Dual Axis Chart) rendered."))
  .catch(console.error);

// ==========================================
// SECTION 4: Cost Drivers & Sector Inequality
// ==========================================

// Chart 11: Farm Cash Cost Composition Streamgraph
vegaEmbed('#chart11-container', 'js/chart11_streamgraph.json', embedOpt)
  .then(result => console.log("Chart 11 (Streamgraph) rendered."))
  .catch(console.error);

// Chart 12: Decile Disparity & Farm Scale Parallel Coordinates
vegaEmbed('#chart12-container', 'js/chart12_parallel_coordinates.json', embedOpt)
  .then(result => console.log("Chart 12 (Parallel Coordinates) rendered."))
  .catch(console.error);