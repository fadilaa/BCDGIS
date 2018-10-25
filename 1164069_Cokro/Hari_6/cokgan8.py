import shapefile    # memasukan module shapefile
w=shapefile.Writer()    # mendefinisikan w sebagai shapefile.writer
w.shapeType     # melakukan penerapan shapeType pada w

w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")   # membuat kolom dengan type character di dalamnya

w.record("ngek","satu")  # membuat rekaman ke satu sebagai tempat [[[1,3],[5,3], [5,2],[1,2],[1,3]]]
w.record("crot","dua")      # membuat rekaman ke satu sebagai tempat [[[1,6],[5,6], [5,9],[1,9],[1,6]]]

w.poly(parts=[[[1,3],[5,3], [5,2],[1,2],[1,3]]],shapeType=shapefile.POLYLINE)   #bentuk garis poli line 
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9],[1,6]]],shapeType=shapefile.POLYLINE)   #bentuk garis poli line 

w.save("cokgan8")   # di simpan dalam bentuk shp dengan nama cokgan8     