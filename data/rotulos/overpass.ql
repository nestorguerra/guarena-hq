// Renovación del extracto de comercios (backlog R-03 y R-12): se ejecuta a mano en https://overpass-api.de/api/interpreter
// y su resultado sustituye a data/guarena.osm para los comercios; la caja es la zona de juego (data/bounds.geojson).
[out:xml][timeout:90][bbox:38.8465,-6.1195,38.8695,-6.0745];
(
  nwr["shop"];
  nwr["amenity"~"^(restaurant|bar|cafe|fast_food|bank|pharmacy|pub)$"];
  nwr["leisure"="fitness_centre"];
  nwr["office"];
  nwr["craft"];
);
out center meta;
