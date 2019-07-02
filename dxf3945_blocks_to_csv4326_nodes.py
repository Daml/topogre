#!/usr/bin/env python
#coding:utf-8

import sys
import pyproj
import dxfgrabber

epsg3945 = pyproj.Proj(init='EPSG:3945')
wgs84 = pyproj.Proj(init='EPSG:4326')

def main(filename):
    print('lng,lat,blockname')
    dxf = dxfgrabber.readfile(filename)

    for entity in dxf.entities:
        if entity.dxftype == 'INSERT':
            coords = pyproj.transform(epsg3945, wgs84, entity.insert[0], entity.insert[1])
            print(repr(coords[0]) + ',' + repr(coords[1]) + ',' + entity.name)

if __name__ == '__main__':
    main(sys.argv[1])

