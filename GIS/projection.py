from pyproj import Proj, transform

inProj = Proj(init='epsg:32610')
outProj = Proj(init='epsg:4326')
x1,y1 = bbox[0], bbox[1]
x2,y2 = transform(inProj,outProj,x1,y1)
x3,y3 = bbox[2], bbox[3]
x4,y4 = transform(inProj,outProj,x3,y3)
print x2,y2,x4,y4
