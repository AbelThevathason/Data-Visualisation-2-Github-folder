// JavaScript tells vegaEmbed: "Take the spec from js/map.json 
// and render it inside the HTML element with id 'map-container'"

vegaEmbed('#map-container', 'js/map.json')
  .then(result => console.log("Map successfully rendered!"))
  .catch(console.error);