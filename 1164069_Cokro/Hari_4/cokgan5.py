import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C") # nama nama kolom
w.field("kolom2","C") # nama nama kolom

w.record("ngek","satu")  # nama record nya ngek hdan satu 

w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) #bentuk garis poli line 

w.save("cokgan5") # di simpan dalam bentuk shp dengan nama cokgan5