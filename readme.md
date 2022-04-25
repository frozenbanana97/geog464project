# Sentinel 1 Downloader & Image Preparation

This project serves to simplify and expedite the downloading and preparation of Sentinel 1 GRD (Ground Range Detected) data, but may prove useful for other kind of single band raster imagery as well.

The Jupyter Notebook will walk you through searching for and downloading the Sentinel 1 imagery utilizing the Alaska Satellite Facility (ASF) [Vertex](https://search.asf.alaska.edu/#/) search API. Through this tool you will be able to WKT (well known text) strings to find relevant satellite imagery for your project. If you do not have a WKT string, you can find one using a geographic point or area in [Vertex](https://search.asf.alaska.edu/#/) with a shapefile of your study area or with the built-in tools.

Going through the entire notebook will extract the data and prepare for your specific study site, providing you with preliminary maps of the study area.

A link to the Binder interactive notebook to experience this project can be found here

[https://mybinder.org/v2/gh/frozenbanana97/geog464project/main?labpath=user-input.ipynb](https://mybinder.org/v2/gh/frozenbanana97/geog464project/main?labpath=user-input.ipynb)
<br>
### Notes

- - -

The requirements.txt had to be remade for the Binder collection as it did not support the manual adding of Fiona, GDAL and Rasterio wheels as is needed when running on Windows. If you want to run this on a venv in Windows you can look at my [documentation](https://github.com/frozenbanana97/documentation) repo for aid in installing these packages.

- - -

<br>
<br>
