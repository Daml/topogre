all: out/mobilier_4326.csv out/mobilier_clean_4326.csv out/armoires.csv osm/armoires.csv

out/mobilier_4326.csv: data/TOPOGRAPHIE_MOBILIER_VDG_EPSG3945.dxf
	python dxf3945_blocks_to_csv4326_nodes.py $< > $@

out/mobilier_clean_4326.csv: mobilier_classes.csv out/mobilier_4326.csv
	python clasify.py out/mobilier_4326.csv > $@

out/armoires.csv: data/TOPOGRAPHIE_MOBILIER_VDG_EPSG3945.dxf
	python armoires.py $< > $@

osm/armoires.csv: refresh armoires.xml
	curl -s -o $@ -X POST -d @armoires.xml https://overpass-api.de/api/interpreter

refresh:
	find osm -name armoires.csv -type f -mtime +10h -delete

clean:
	rm -rf out/*
	rm -rf osm/*

.PHONY: clean refresh
