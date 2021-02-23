# Author: Daniel Mutton
# Date: Oct 3, 2019
# Title: Geomorphometric Variable Calculator
# Purpose: To take an input elevation raster, calculate several geomorphometric variables and export each as their own raster file

import os, sys
import numpy as np
from osgeo import gdal, osr
from osgeo.gdalconst import *
from sympy import symbols, diff

print(np.intp)
gdal.AllRegister()
gdal.UseExceptions()

# Open Image
# specify DEM location in fpath
fpath = ('')
inRas = gdal.Open(fpath)
if inRas is None:
  print ('Could not open image file')
  sys.exit(1)

# read in the crop data and get info about it
band1 = inRas.GetRasterBand(1)
rows = inRas.RasterYSize
cols = inRas.RasterXSize

cropData = band1.ReadAsArray(0,0,cols,rows)

transform = inRas.GetGeoTransform()

xOrigin = transform[0] # x origin
yOrigin = transform[3] # y origin
pixWidth = transform[1] # pixel width
pixHeight = transform[5] # pixel height

#Create array with lat/long/elevation
complete_array = []
numrows = len(cropData)
numcols = len(cropData[0])
ymax = 0
ymin = 0
xmax = 0
ymin = 0

complete_array = []
numrows = len(cropData)
numcols = len(cropData[0])

for row in range(numrows):
  row_list = []
  for col in range(numcols):
    latitude = yOrigin + (row * pixHeight)
    if col ==0:
      ymin = latitude
      ymax = latitude
    if latitude > ymax:
      ymin = latitude
    if latitude < ymin:
      ymax = latitude
      
    longitude = xOrigin + (col * pixWidth)
    if col ==0:
      xmin = longitude
      xmax = longitude
    if longitude > xmax:
      xmin = longitude
    if longitude < xmax:
      xmax = longitude

    elevation = cropData[row,col]
    latitude = yOrigin + (row * pixHeight)
    longitude = xOrigin + (col * pixWidth)
    elevation = cropData[row,col]
    col_list = [latitude, longitude,elevation]
    row_list.append(col_list)
    
  complete_array.append(row_list)
  


print(complete_array[1][1][2])

# Calculate partial derivatives
#by default it creates the g partial derivative. Other partial derivates are included and can be commented out/in
g_array = []

for row in range(rows):
  if row % 100 == 0:
    print("row " + str(row+1))
  new = []
  for col in range(cols):   
    try:
      z1 = float(complete_array[row-2][col-2][2])
    except ValueError:
      z1 = (float(complete_array[row][col][2])-float(complete_array[row+2][col+2][2]))/(0-14.142)*14.142
    except IndexError:
      z1 = -9999
    try:  
      z2 = float(complete_array[row-2][col-1][2])
    except ValueError:
      z2 = (float(complete_array[row][col][2])-float(complete_array[row+2][col+1][2]))/(0-11.18)*11.18
    except IndexError:
      z2 = -9999
    try:
      z3 = float(complete_array[row-2][col][2])
    except ValueError:
      z3 = (float(complete_array[row][col][2])-float(complete_array[row+2][col][2]))/(0-10)*10
    except IndexError:
      z3 = -9999
    try:
      z4 = float(complete_array[row-2][col+1][2])
    except ValueError:
      z4 = (float(complete_array[row][col][2])-float(complete_array[row+2][col-1][2]))/(0-11.18)*11.18
    except IndexError:
      z4 = -9999
    try:
      z5 = float(complete_array[row-2][col+2][2])
    except ValueError:
      z5 = (float(complete_array[row][col][2])-float(complete_array[row+2][col-2][2]))/(0-14.142)*14.142
    except IndexError:
      z5 = -9999
      
    try:
      z6 = float(complete_array[row-1][col-2][2])
    except ValueError:
      z6 = (float(complete_array[row][col][2])-float(complete_array[row+1][col+2][2]))/(0-11.18)*11.18
    except IndexError:
      z6 = -9999
    try:
      z7 = float(complete_array[row-1][col-2][2])
    except ValueError:
      z7 = (float(complete_array[row][col][2])-float(complete_array[row+2][col+2][2]))/(0-14.142)*7.071
    except IndexError:
      z7 = -9999
    try:
      z8 = float(complete_array[row-1][col][2])
    except ValueError:
      z8 = (float(complete_array[row][col][2])-float(complete_array[row+2][col][2]))/(0-10)*5
    except IndexError:
      z8 = -9999
    try:
      z9 = float(complete_array[row-1][col+1][2])
    except ValueError:
      z9 = (float(complete_array[row][col][2])-float(complete_array[row+2][col-2][2]))/(0-14.142)*7.071
    except IndexError:
      z9 = -9999
    try:
      z10 = float(complete_array[row-1][col+2][2])
    except ValueError:
      z10 = (float(complete_array[row][col][2])-float(complete_array[row+1][col-2][2]))/(0-11.18)*11.18
    except IndexError:
      z10 = -9999

    try:
      z11 = float(complete_array[row][col-2][2])
    except ValueError:
      z11 = (float(complete_array[row][col][2])-float(complete_array[row][col+2][2]))/(0-10)*10
    except IndexError:
      z11 = -9999
    try:
      z12 = float(complete_array[row][col-1][2])
    except ValueError:
      z12 = (float(complete_array[row][col][2])-float(complete_array[row][col+2][2]))/(0-10)*5
    except IndexError:
      z12 = -9999
    try:
      z13 = float(complete_array[row][col][2])
    #Same as z12
    except ValueError:
      z12 = (float(complete_array[row][col][2])-float(complete_array[row][col+2][2]))/(0-10)*5  
    except ValueError:
      z13 = -9999
    try:
      z14 = float(complete_array[row][col+1][2])
    except ValueError:
      z14 = (float(complete_array[row][col][2])-float(complete_array[row][col-2][2]))/(0-10)*5
    except IndexError:
      z14 = -9999
    try:
      z15 = float(complete_array[row][col+2][2])
    except ValueError:
      z15 = (float(complete_array[row][col][2])-float(complete_array[row][col-2][2]))/(0-10)*10
    except IndexError:
      z15 = -9999

    try:
      z16 = float(complete_array[row+1][col-2][2])
    except ValueError:
      z16 = (float(complete_array[row][col][2])-float(complete_array[row-1][col+2][2]))/(0-11.18)*11.18
    except IndexError:
      z16 = -9999
    try:
      z17 = float(complete_array[row+1][col-1][2])
    except ValueError:
      z17 = (float(complete_array[row][col][2])-float(complete_array[row-2][col+2][2]))/(0-14.142)*7.071
    except IndexError:
      z17 = -9999
    try:
      z18 = float(complete_array[row+1][col][2])
    except ValueError:
      z18 = (float(complete_array[row][col][2])-float(complete_array[row-2][col][2]))/(0-10)*5
    except IndexError:
      z18 = -9999
    try:
      z19 = float(complete_array[row+1][col+1][2])
    except ValueError:
      z19 = (float(complete_array[row][col][2])-float(complete_array[row-2][col-2][2]))/(0-14.142)*7.071
    except IndexError:
      z19 = -9999
    try:
      z20 = float(complete_array[row+1][col+2][2])
    except ValueError:
      z20 = (float(complete_array[row][col][2])-float(complete_array[row-1][col-2][2]))/(0-11.18)*11.18
    except IndexError:
      z20 = -9999

    try:
      z21 = float(complete_array[row+2][col-2][2])
    except ValueError:
      z21 = (float(complete_array[row][col][2])-float(complete_array[row-2][col+2][2]))/(0-14.142)*14.142
    except IndexError:
      z21 = -9999
    try:
      z22 = float(complete_array[row+2][col-1][2])
    except ValueError:
      z22 = (float(complete_array[row][col][2])-float(complete_array[row-2][col+1][2]))/(0-11.18)*11.18
    except IndexError:
      z22 = -9999
    try:
      z23 = float(complete_array[row+2][col][2])
    except ValueError:
      z23 = (float(complete_array[row][col][2])-float(complete_array[row-2][col][2]))/(0-10)*10
    except IndexError:
      z23 = -9999
    try:
      z24 = float(complete_array[row+2][col+1][2])
    except ValueError:
      z24 = (float(complete_array[row][col][2])-float(complete_array[row-2][col-1][2]))/(0-11.18)*11.18
    except IndexError:
      z24 = -9999
    try:
      z25 = float(complete_array[row+2][col+2][2])
    except ValueError:
      z25 = (float(complete_array[row][col][2])-float(complete_array[row-2][col-2][2]))/(0-14.142)*14.142
    except IndexError:
      z25 = -9999
        
    g = (1/1250)*(z5+z10+z15+z20+z25-z1-z6-z11-z16-z21+2*(z2+z7+z12+z17+z22-z4-z9-z14-z19-z24))                             #1/10*w^3
##    h = (1/1250)*(z1+z2+z3+z4+z5-z21-z22-z23-z24-z25+2*(z16+z17+z18+z19+z20-z6-z7-z8-z9-z10))                               #1/10*w^3
##    k = (1/8750)*(z7+z17-z9-z19+4*(z5+z11+z25-z1-z15-z21)+2*(z4+z6+z12+z24-z2-z4-z8-z16-z20))                               #1/70*w^3
##    m = (1/8750)*(z7+z17-z9-z19+4*(z5+z11-z1-z15-z21)+2*(z4+z6+z12+z16+z24-z2-z10-z14-z20-z22))                             #1/70*w^3
##    r = (1/875)*(2*(z1+z5+z6+z10+z11+z15+z16+z21+z25)-2*(z3+z8+z13+z18+z23)-z2-z4-z7-z9-z12-z14-z19-z22-z24)                #1/35*w^2
##    t = (1/875)*(2*(z1+z2+z3+z4+z5+z21+z22+z23+z24+z25)-2*(z11+z12+z13+z14+z15)-z6-z7-z8-z9-z10-z16-z17-z19-z22-z24)        #1/35*w^2
##    s = (1/2500)*(z9+z17-z7-z19+4*(z5+z21-z1-z25)+2*(z4+z10+z16+z22-z2-z6-z20-z24))                                         #1/100*w^2
##    p = (1/2100)*(44*(z4+z24-z2-z22)+31*(z1+z21-z5-z25+2*(z9+z19-z7-z17))+17*(z15-z11+4*(z14-z15))+5*(z10+z20-z6-z16))      #1/420*w
##    q = (1/2100)*(44*(z6+z10-z16-z20)+31*(z21+z24-z1-z5+2*(z7+z9-z17-z19))+17*(z3-z23+4*(z8-z18))+5*(z2+z4-z22-z24))        #1/420*w

    new.append(g)
  g_array.append(new)

#Write array to raster
xres = pixWidth
yres = pixHeight
geotransform=(xOrigin,pixWidth,0,yOrigin,0, pixHeight)


#Nova Scotia Scotts Bay Area - EPSG 4269. Manacouagan Peninsula - 26919
# change Create('') to the name of the file you want to save, use .tif file format
output_raster = gdal.GetDriverByName('GTiff').Create('',cols, rows, 1 ,gdal.GDT_Float32)
output_raster.SetGeoTransform(geotransform)
srs = osr.SpatialReference()
srs.ImportFromEPSG(26919)

output_raster.SetProjection( srs.ExportToWkt() )
temp1 = output_raster.GetRasterBand(1)
temp2 = np.asarray(g_array, dtype=np.float32)
temp3 = temp1.WriteArray(temp2)
output_raster = None

print("done")
