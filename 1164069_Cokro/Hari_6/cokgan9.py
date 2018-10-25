import shapefile    # memasukan module shapefile
w=shapefile.Writer()    # mendefinisikan w sebagai shapefile.writer
w.shapeType     # melakukan penerapan shapeType pada w

w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")   # membuat kolom dengan type character di dalamnya

w.record("belahketupat","enak") # membuat rekaman ke satu sebagai tempat [[[1,2],[2,3], [3,2],[2,1],[1,2]]]
w.record("belahketupat","sedap")    # membuat rekaman ke satu sebagai tempat  [[[0,2],[2,4], [4,2],[2,0],[0,2]]]
w.record("belahketupat","mantap")   # membuat rekaman ke satu sebagai tempat [[[-1,2],[2,5], [5,2],[2,-1],[-1,2]]]
w.record("belahketupat","syurlodeh")    # membuat rekaman ke satu sebagai tempat [[[-2,2],[2,6], [6,2],[2,-2],[-2,2]]]
w.record("belahketupat","pahaayam") # membuat rekaman ke satu sebagai tempat [[[-3,2],[2,7], [7,2],[2,-3],[-3,2]]]
w.record("belahketupat","gulaikambing") # membuat rekaman ke satu sebagai tempat [[[-4,2],[2,8], [8,2],[2,-4],[-4,2]]]

w.poly(parts=[[[1,2],[2,3], [3,2],[2,1],[1,2]]],shapeType=shapefile.POLYLINE)   #bentuk garis poli line
w.poly(parts=[[[0,2],[2,4], [4,2],[2,0],[0,2]]],shapeType=shapefile.POLYLINE)   #bentuk garis poli line
w.poly(parts=[[[-1,2],[2,5], [5,2],[2,-1],[-1,2]]],shapeType=shapefile.POLYLINE) #bentuk garis poli line
w.poly(parts=[[[-2,2],[2,6], [6,2],[2,-2],[-2,2]]],shapeType=shapefile.POLYLINE) #bentuk garis poli line
w.poly(parts=[[[-3,2],[2,7], [7,2],[2,-3],[-3,2]]],shapeType=shapefile.POLYLINE) #bentuk garis poli line
w.poly(parts=[[[-4,2],[2,8], [8,2],[2,-4],[-4,2]]],shapeType=shapefile.POLYLINE) #bentuk garis poli line

w.save("cokgan9") # di simpan dalam bentuk shp dengan nama cokgan9      