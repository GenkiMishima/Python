#!/usr/bin/env python3
import Functions as Fs 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    Osaka = 34.702113, 135.494807
    Tokyo = 35.681541, 139.767103
    London = 51.476853, 0.0

    n=10

    #print(Fs.GetPath(Osaka, Tokyo, n))
    #print(Fs.dist_on_sphere(Osaka, Tokyo))

    Elevation = Fs.GetPath(Osaka, Tokyo, n)
    Distance = Fs.dist_on_sphere(Osaka, Tokyo)

    plt.plot(Elevation)
    plt.show()
