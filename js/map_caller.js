// JavaScript tells vegaEmbed: "Take the spec from js/map.json 
// and render it inside the HTML element with id 'map-container'"

vegaEmbed('#map-container', 'js/map.json')
  .then(result => console.log("Map successfully rendered!"))
  .catch(console.error);
// 2. Render Map Idiom 2 (Proportional Symbol Map) into #map-container-2
vegaEmbed('#map-container-2', 'js/map2.json', { "actions": false })
  .then(result => console.log("Map 2 rendered."))
  .catch(console.error);
vegaEmbed('#map-container-3', 'js/map3.json', { "actions": false })
  .then(result => console.log("Map 3 rendered."))
  .catch(console.error);