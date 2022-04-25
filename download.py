#import requirements
import asf_search as asf
import getpass
from shapely import wkt
import os.path
from os import mkdir
from os import listdir
from datetime import date, datetime

#define the location of the study area usiong a WKT
def location():
   wktlocation = input('input WKT string')
   print('The given location is: ' + wktlocation)
   return wktlocation

#define and check start date of geographic search
def startDate():
    dateStart = input('input start date in YYYY-MM-DD')
    format = '%Y-%m-%d'
    startRes = True
    endRes = True
    try:
        startRes = bool(datetime.strptime(dateStart, format))
    except ValueError:
        startRes = False
        
    print('Start Date: ' + dateStart)
    print("Does start date match format? : " + str(startRes))
    return dateStart

#define and check end date of geographic search
def endDate():
    dateEnd = input('input end date in YYYY-MM-DD')
    format = '%Y-%m-%d'
    startRes = True
    endRes = True
    try:
        endRes = bool(datetime.strptime(dateEnd, format))
    except ValueError:
        endRes = False
    
    print('End Date: ' + dateEnd)
    print("Does end date match format? : " + str(endRes))    
    return dateEnd

#perform the search for relevant products using ASF's search API module using shape-WKT
def geo_loc(wktlocation, dateStart, dateEnd):
    geo_results = asf.geo_search(
        intersectsWith=wktlocation,
        platform=asf.PLATFORM.SENTINEL1,
        maxResults=10,
        start=dateStart,
        end=dateEnd)

    print(f'{len(geo_results)} results found')
    return geo_results

#perform the search for relevant products using ASF's search API module using centroid-WKT
def centroid_loc(wktlocation, dateStart, dateEnd):
    centroidwkt = wkt.loads(wktlocation)
    centroid = centroidwkt.centroid.wkt

    centroid_results = asf.geo_search(
        intersectsWith=centroid,
        platform=asf.PLATFORM.SENTINEL1,
        maxResults=10,
        start=dateStart,
        end=dateEnd)

    print(f'{len(centroid_results)} results found')
    return centroid_results

#perform the search for relevant products using ASF's search API module using scene names
def scene_loc(scene_list):
    granule_results = asf.granule_search(scene_list)

    print(f'{len(granule_results)} results found')
    return granule_results

#set the downlaod directory, or create it if it doesnt exist
def dir_create():
    downPath = './downloads'
    isDir = os.path.isdir(downPath)

    if isDir == False:
        mkdir('downloads')

#prompt to login to ASF Search for download
def ASF_login():
    dirs = ['downloads']

    #login to ASF using EE credentials
    username = input('Username:')
    password = getpass.getpass('Password:')

    try:
        user_pass_session = asf.ASFSession().auth_with_creds(username, password)
    except asf.ASFAuthenticationError as e:
        print(f'Auth failed: {e}')
    else:
        print('Success!')
    return user_pass_session

#download the found products to directory
def download_products(results, user_session):
    results.download(path='./downloads', session=user_session)

    listdir('./downloads')

