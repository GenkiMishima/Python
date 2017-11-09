#!/usr/bin/env python3
import Functions as Fs
import matplotlib.pyplot as plt

if __name__ == "__main__":
    point1 = 35.300070,138.933728#御殿場駅
    point2 = 35.221630,138.615337#富士宮駅
    point3 = 35.483352,138.795616#富士山駅

    print(u"Distance:"+str(Fs.GetPathDistance(point1,point2))+"\n")
    print(u"Distance:"+str(Fs.GetPathDistance(point1,point3))+"\n")
    print(u"Elevation:"+str(Fs.GetPathElevation(point2,point3))+"\n")
    
