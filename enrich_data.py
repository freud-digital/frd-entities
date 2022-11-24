from baserow_utils import enrich_data


TABLE_ID = "1474"
enrich_data(br_table_id=TABLE_ID, uri="gnd", field_name_input={"gnd": "gnd_id", "wikidata": "wikidata"}, field_name_update={"wikidata":"wikidata", "gnd": "gnd_id"})

TABLE_ID = "1468"
enrich_data(br_table_id=TABLE_ID, uri="geonames", field_name_input={"gnd": "gnd_id", "geonames": "geonames_id", "wikidata": "wikidata"}, field_name_update={"wikidata": "wikidata", "gnd": "gnd_id", "geonames": "geonames_id"})

TABLE_ID = "1476"
enrich_data(br_table_id=TABLE_ID, uri="gnd", field_name_input={"gnd": "gnd_id", "geonames": "geonames_id", "wikidata": "wikidata"}, field_name_update={"wikidata": "wikidata", "gnd": "gnd_id", "geonames": "geonames_id"})