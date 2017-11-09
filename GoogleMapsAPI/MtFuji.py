#!/usr/bin/env python3
import Functions as Fs
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    point1 = 35.300070,138.933728#御殿場駅
    point2 = 35.221630,138.615337#富士宮駅
    point3 = 35.483352,138.795616#富士山駅


    PO1 = np.array([point1[0],point1[1]])#GoogleMapAPI用
    PO2 = np.array([point2[0],point2[1]])#GoogleMapAPI用
    PO3 = np.array([point3[0],point3[1]])#GoogleMapAPI用

    #P1 = PO1-PO1#初期化
    #P2 = PO2-PO1#初期化
    #P3 = PO3-PO1#初期化


    m=3.0
    n=3.0


    dx=P2[0]/n
    dy=P3[0]/m

    Dis = np.array(Fs.GetPathDistance(PO1,PO2))
    Ele = np.array(Fs.GetPathElevation(PO1,PO2,n))

    #print (Ele)













    print (str(P1)+","+str(P2)+","+str(P3))
    print(u"Distance:"+str(Fs.GetPathDistance(PO1,PO2))+"\n")
    print(u"Distance:"+str(Fs.GetPathDistance(point1,point3))+"\n")
    print(u"Elevation:"+str(Fs.GetPathElevation(point1,point2))+"\n")
    
