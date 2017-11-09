#!/usr/bin/env python3
import urllib.request
import simplejson
from urllib.request import urlparse
import googlemaps
from math import sin,cos,acos,radians

earth_rad = 6378137#[m]

ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json?'
MY_GOOGLE_ELEVATION_API_CODE = "AIzaSyD41MKIhl34BS66pFxcY1jELsQ0x2pgric"
MY_GOOGLE_GEOCODING_API_CODE = "AIzaSyAtHNHHTJZX7wDKEma1YIk8GJXdMVL_rOE"
SAVE_DATA_NAME = 'test.png'

gmaps = googlemaps.Client(key=MY_GOOGLE_GEOCODING_API_CODE)

def GetElevation(pointX,pointY):
    URL = ELEVATION_BASE_URL+'locations=' + str(pointX) +','+ str(pointY) + '&key=' + MY_GOOGLE_ELEVATION_API_CODE
    #print(URL)
    data = urllib.request.urlopen(URL).read()
    response = simplejson.load(urllib.request.urlopen(URL))

    elevationArray = []
    for resultset in response['results']:
        elevationArray.append(resultset['elevation'])
    return elevationArray


def GetPathElevation(point1,point2,n=10):
    URL = ELEVATION_BASE_URL+'path='+str(point1[0])+','+str(point1[1])+'|'+str(point2[0])+','+str(point2[1])+'&samples='+ str(n)+'&key='+MY_GOOGLE_ELEVATION_API_CODE
    #print(URL)
    data = urllib.request.urlopen(URL).read()
    response = simplejson.load(urllib.request.urlopen(URL))

    elevationArray = []
    for resultset in response['results']:
        elevationArray.append(resultset['elevation'])
    return elevationArray


def latlng_to_xyz(lat,lng):
    rlat,rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng),sin(rlat)

def GetPathDistance(pos0, pos1, radious=earth_rad):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x*y for x, y in zip(xyz0,xyz1)))*radious




if __name__ == "__main__":
    print (u'======================FunctionTest==========================')


    print (u'=====================FunctionTestEnd========================')
