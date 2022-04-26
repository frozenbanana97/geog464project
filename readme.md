# Sentinel 1 Downloader & Image Preparation

This project serves to simplify and expedite the downloading and preparation of Sentinel 1 GRD (Ground Range Detected) data, but may prove useful for other kind of single band raster imagery as well.

The Jupyter Notebook will walk you through searching for and downloading the Sentinel 1 imagery utilizing the Alaska Satellite Facility (ASF) [Vertex](https://search.asf.alaska.edu/#/) search API. Through this tool you will be able to WKT (well known text) strings to find relevant satellite imagery for your project. If you do not have a WKT string, you can find one using a geographic point or area in [Vertex](https://search.asf.alaska.edu/#/) with a shapefile of your study area or with the built-in tools.

Going through the entire notebook will extract the data and prepare for your specific study site, providing you with preliminary maps of the study area.


## Notes

A Earthdata login is required to download the data using this module, I have provided some data here you can download to bypass this, it has been downloaded and georeferenced and should be placed somewhere within the working directory.

- - -

~~The requirements.txt had to be remade for the Binder collection as it did not support the manual adding of Fiona, GDAL and Rasterio wheels as is needed when running on Windows. If you want to run this on a venv in Windows you can look at my [documentation](https://github.com/frozenbanana97/documentation) repo for aid in installing these packages. requirements.txt.bak are the Windows requirements whereas requirements.txt was made solely for Binder.~~<br><br>
I have been unable to et GDAL to work within Binder, therefore I ask that you clone and run this repo manually with your owm virtual environment if you want to view it. I have provided the Windows Wheel dependencies needed to install the requirements, thank you for your understanding.

- - -
