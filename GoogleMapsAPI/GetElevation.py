#!/usr/bin/env python3
import Functions as Fs 

if __name__ == "__main__":
    pointX = 35.68037
    pointY = 139.7666913
    Elevation = Fs.GetElevation(pointX,pointY)
    print (Elevation)
