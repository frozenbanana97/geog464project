import zipfile
from pathlib import Path
import fiona
import rasterio
import rasterio.mask
from rasterio import plot
from rasterio.plot import show
import numpy as np
import matplotlib
from matplotlib import pyplot


def unzip():
    p = Path('.')
    
    for f in p.glob('downloads/*.zip'):
        with zipfile.ZipFile(f, 'r') as archive:
            archive.extractall(path=f'./downloads/{f.stem}')
            print(f'Done {f.stem}')

def clip():

    shapefile = input('input directory of shapefile to clip extents with, including file name')
    rastin = input('input directory of raster image, including file name')
    rastout = input('output directory for clipped file, including file name')
    
    p = Path('.')

    crs = rasterio.crs.CRS({"init": "epsg:4326"})
    
    with fiona.open(shapefile, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

    with rasterio.open(rastin) as src:
            #src.crs = crs #could not figure this one out... have to open the tif is QGIS and export/saveAs it with the proper CRS. I have provided sample geotiffs in the data directory
            out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
            out_meta = src.meta
            out_meta.update({"driver": "GTiff",
             "height": out_image.shape[1],
             "width": out_image.shape[2],
             "transform": out_transform})

    with rasterio.open(rastout, "w", **out_meta) as dest:
        dest.write(out_image)

def reclass():
    rastin = input('input directory of raster image to reclassify, including file name')
    rastout = input('output directory of reclassified image, including file name')
    ds = rasterio.open(rastin)
    data = ds.read()
    max = data.max()
    mean = data.mean()

    lista = data.copy()

    lista[np.where((lista >= 0) & (lista <= mean/2))] = 1 #deforested
    lista[np.where((lista >= mean/2) & (lista <= mean))] = 2 #meh
    lista[np.where((lista >= mean) & (lista <= max))] = 3 #forest

    with rasterio.open(rastout, 'w', 
    driver=ds.driver,
    height=ds.height,
    width=ds.width,
    count=ds.count,
    transform=ds.transform,
    dtype=data.dtype) as dst:
        dst.write(lista)

def present_maps():
