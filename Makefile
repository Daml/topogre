all: out/mobilier_4326.csv out/mobilier_clean_4326.csv

out/mobilier_4326.csv: data/TOPOGRAPHIE_MOBILIER_VDG_EPSG3945.dxf
	python dxf3945_blocks_to_csv4326_nodes.py $< > $@

out/mobilier_clean_4326.csv: mobilier_classes.csv out/mobilier_4326.csv
	python clasify.py out/mobilier_4326.csv > $@

clean:
	rm -rf out

.PHONY: clean
