all: out/mobilier_4326.csv

out/mobilier_4326.csv: data/TOPOGRAPHIE_MOBILIER_VDG_EPSG3945.dxf
	python dxf3945_blocks_to_csv4326_nodes.py $< > $@

clean:
	rm -rf out

.PHONY: clean
