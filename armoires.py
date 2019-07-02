#!/usr/bin/env python
#coding:utf-8

import sys
import pyproj
import math
import dxfgrabber

epsg3945 = pyproj.Proj(init='EPSG:3945', preserve_units=True)
wgs84 = pyproj.Proj(init='EPSG:4326')

def main(filename):
    print("handle\tlng\tlat\twidth\tprof")
    dxf = dxfgrabber.readfile(filename)

    for entity in dxf.entities:
        if entity.dxftype == 'INSERT' and entity.name == 'MOB037_4':
            # Unitées ?
            width = entity.scale[0] * 1.2
            prof = entity.scale[1] * 1.2

            # Point d'insertion
            base = entity.insert

            # Offset de base
            xo = width * math.cos(math.radians(entity.rotation))
            yo = width * math.sin(math.radians(entity.rotation))

            # Points cardinaux
            sw = (base[0], base[1])
            se = (base[0] + xo, base[1] + yo)
            nw = (base[0] + prof * math.cos(math.radians(entity.rotation + 90)), base[1] + prof * math.sin(math.radians(entity.rotation + 90)))
            ne = (nw[0] + xo, nw[1] + yo)

            # Moyenne du centre
            x = (sw[0] + se[0] + ne[0] + nw[0]) / 4
            y = (sw[1] + se[1] + ne[1] + nw[1]) / 4

            # Reprojection
            coords = pyproj.transform(epsg3945, wgs84, x, y)

            print("%s\t%.32f\t%.32f\t%f\t%f" % (entity.handle, coords[0], coords[1], round(width, 2), round(prof, 2)))

if __name__ == '__main__':
    main(sys.argv[1])

