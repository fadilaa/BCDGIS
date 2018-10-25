import shapefile    # memasukan module shapefile
w=shapefile.Writer()    # mendefinisikan w sebagai shapefile.writer
w.shapeType     # melakukan penerapan shapeType pada w

w.field("kolom1","C") # membuat kolom dengan type character di dalamnya
w.field("kolom2","C") # membuat kolom dengan type character di dalamnya

w.record("ngek","satu")  # membuat rekaman ke satu sebagai tempat semua titik koordianat

w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) #bentuk garis poli line 

w.save("cokgan5") # di simpan dalam bentuk shp dengan nama cokgan5