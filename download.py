#import requirements
import asf_search as asf
import getpass
from shapely import wkt
import os.path
from os import mkdir
from os import listdir


#perform the search for results with the given location and date range, use if centroid yields no results

def geo_loc(location, dateStart, dateEnd):
    geo_results = asf.geo_search(
        intersectsWith=location,
        platform=asf.PLATFORM.SENTINEL1,
        maxResults=10,
        start=dateStart,
        end=dateEnd)

    print(f'{len(geo_results)} results found')

def centroid_loc(location, dateStart, dateEnd):
    centroidwkt = wkt.loads(location)
    centroid = centroidwkt.centroid.wkt

    centroid_results = asf.geo_search(
        intersectsWith=centroid,
        platform=asf.PLATFORM.SENTINEL1,
        maxResults=10,
        start=dateStart,
        end=dateEnd)

    print(f'{len(centroid_results)} results found')

def scene_download(scene_list):
    granule_results = asf.granule_search(scene_list)

    print(f'{len(granule_results)} results found')

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

def download_products(results, user_pass_session):
    results.download(path='./downloads', session=user_pass_session)

    listdir('./downloads')
