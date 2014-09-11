from Graphics import *
from random import *
from math import *
from time import sleep

size = 512

win = Window("Midpoint Displacement", size, size)

smoothness = .85

mountains = 5

heightData = []
for x in range(size + 1):
    heightData.append(0)


def midpointDisplacement(a, b, color):
    midpoint = calcMidpoint(a,b)
    midheight = getMidpointHeight(a,b)
    
    heightData[int(midpoint)] = midheight + Noise(a, b, smoothness)
    
    graphData(midpoint, color)
    
    if (midpoint - a > 1):
        midpointDisplacement(a, midpoint, color)
    if (b - midpoint > 1):
        midpointDisplacement(midpoint, b, color)
    else:
        return
    

def calcMidpoint(a, b):
    return int((a+b)/2)
    
def getMidpointHeight(a, b):
    return (heightData[a] + heightData[b])/2

def graphData(x, color):
        heightData[x] = floor(heightData[x])
        testShape = Line((x,heightData[x]), (x,size))
        
        testShape.color = Color(color)
        
        testShape.draw(win)

        
        sleep(0.0001)

def Noise(a, b, smoothness):
    maxNoise = (int)((b-a)/(smoothness * 4))
    return randint(0, 2 * maxNoise) - maxNoise
      
def initHeight(size):
       return randint((int)(size / 4), (int)(size / 4 * 3))
          
for x in range(size):
     otherShape = Line((x,0), (x, size))
     otherShape.color = Color('lightblue')
     otherShape.draw(win)

heightData[0] = initHeight(size)
heightData[size] = initHeight(size)

for mountain in range(mountains):
    heightData[0] = heightData[0] + (5 * mountain)
    heightData[size] = heightData[size] + (5 * mountain)
    midpointDisplacement(0, size, Color(255-(255/(mountain+1)), 255-(255/(mountain+1)), 255-(255/(mountain+1))))
    print("Iteration:", mountain+1)    






