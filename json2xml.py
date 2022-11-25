from baserow_utils import make_xml, make_geojson


data = {
    "persons": "json_dumps/persons.json",
    "places": "json_dumps/places.json",
    "org": "json_dumps/orgs.json",
    "keyword": "json_dumps/keywords.json",
    "dream": "json_dumps/dreams.json"
}

listperson = make_xml(data["persons"], "listperson", "gnd", "persons")
listplace = make_xml(data["places"], "listplace", "geonames_id", "places")
listorg = make_xml(data["org"], "listorg", "wikidata", "orgs")
listkey = make_xml(data["keyword"], "listkey", False, "keywords")
listdream = make_xml(data["dream"], "listdream", False, "dreams")

placejson = make_geojson(data["places"], "listplace", "geonames_coordinates", "google_maps_coordinates", "located_in")
orgjson = make_geojson(data["org"], "listorg", "geonames_coordinates", "google_maps_coordinates", "located_in")