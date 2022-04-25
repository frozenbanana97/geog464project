#import requirements
import asf_search as asf
import getpass
from shapely import wkt
import os.path
from os import mkdir
from os import listdir
from datetime import date, datetime

def location():
   wktlocation = input('input WKT string')
   print('The given location is: ' + wktlocation)
   return wktlocation

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

def geo_loc(wktlocation, dateStart, dateEnd):
    geo_results = asf.geo_search(
        intersectsWith=wktlocation,
        platform=asf.PLATFORM.SENTINEL1,
        maxResults=10,
        start=dateStart,
        end=dateEnd)

    print(f'{len(geo_results)} results found')
    return geo_results

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

def scene_loc(scene_list):
    granule_results = asf.granule_search(scene_list)

    print(f'{len(granule_results)} results found')
    return granule_results

def dir_create():
    #set the downlaod directory, or create it if it doesnt exist
    downPath = './downloads'
    isDir = os.path.isdir(downPath)

    if isDir == False:
        mkdir('downloads')

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

def download_products(results, user_session):
    results.download(path='./downloads', session=user_session)

    listdir('./downloads')

