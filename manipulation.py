#import requirements
import zipfile
from pathlib import Path
import fiona
import rasterio
import rasterio.mask
from rasterio import plot
from rasterio.plot import show
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar

#unzip all files in the downloads directory
def unzip():
    p = Path('.')
    
    for f in p.glob('downloads/*.zip'):
        with zipfile.ZipFile(f, 'r') as archive:
            archive.extractall(path=f'./downloads/{f.stem}')
            print(f'Done {f.stem}')

#clip function using user input to clip/mask to desired study area
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

#reclassifying the images to reduce number of classes from normal (~900) to just 3 for easier viewing
def reclass():
    rastin = input('input directory of raster image to reclassify, including file name')
    rastout = input('output directory of reclassified image, including file name')
    ds = rasterio.open(rastin)
    data = ds.read()
    max = data.max()
    mean = data.mean()

    lista = data.copy()

    lista[np.where((lista >= 0) & (lista <= mean/2))] = 1 #deforested
    lista[np.where((lista >= mean/2) & (lista <= mean))] = 2 #middle
    lista[np.where((lista >= mean) & (lista <= max))] = 3 #forest

    with rasterio.open(rastout, 'w', 
    driver=ds.driver,
    height=ds.height,
    width=ds.width,
    count=ds.count,
    transform=ds.transform,
    dtype=data.dtype) as dst:
        dst.write(lista)

#map generator to creapt PNG maps of the study area(s)
def present_maps():
    rastin = input('input directory of raster image to map, including file name')
    mapName = input('input name of map, no spaces')

    src = rasterio.open(rastin)
    fig, ax = plt.subplots(1, figsize=(12, 12))
    show((src, 1), cmap='Greens', interpolation='none', ax=ax)
    #add scalebar
    ax.add_artist(ScaleBar(1.5, dimension= "si-length", units="m", location= 'lower right'))
    #add north arrow
    x, y, arrow_length = 0.05, 0.97, 0.075
    ax.annotate('N', xy=(x, y), xytext=(x, y-arrow_length),
                arrowprops=dict(facecolor='black', width=5, headwidth=20),
                ha='center', va='center', fontsize=20,
                xycoords=ax.transAxes)
    #Add Map Title
    ax.annotate(
        mapName,
        (0.5,1)
        ,xycoords = 'axes fraction'
        ,horizontalalignment='center'
        ,verticalalignment='bottom'
        ,fontsize = 20
        ,color='#000'
        ,fontstyle='normal'
    )
    plt.savefig(mapName +'.png', dpi=600)

