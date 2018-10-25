import shapefile # memasukan module shapefile
w=shapefile.Writer() # mendefinisikan w sebagai shapefile.writer
w.shapeType # melakukan penerapan shapeType pada w

w.field("kolom1","C") # membuat kolom dengan  type data char
w.field("kolom2","C") # membuat kolom dengan  type data char

w.record("S","E") # membuat rekaman ke satu sebagai tempat [[[1,1],[3,4], [5,1],[1,1]]]
w.record("G","I") # membuat rekaman ke satu sebagai tempat [[[5,1],[7,4], [3,4],[5,1]]]
w.record("T","I") # membuat rekaman ke satu sebagai tempat [[[1,1],[-1,4], [3,4],[1,1]]]
w.record("G","A") # membuat rekaman ke satu sebagai tempat [[[-1,-2],[1,1], [3,-2],[-1,-2]]]
w.record("Sa","MA") # membuat rekaman ke satu sebagai tempat [[[1,1],[3,-2], [5,1],[1,1]]]
w.record("Ka","Ki") # membuat rekaman ke satu sebagai tempat [[[3,-2],[5,1], [7,-2],[3,-2]]]




w.poly(parts=[[[1,1],[3,4], [5,1],[1,1]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE
w.poly(parts=[[[5,1],[7,4], [3,4],[5,1]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE
w.poly(parts=[[[1,1],[-1,4], [3,4],[1,1]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE
w.poly(parts=[[[-1,-2],[1,1], [3,-2],[-1,-2]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE
w.poly(parts=[[[1,1],[3,-2], [5,1],[1,1]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE
w.poly(parts=[[[3,-2],[5,1], [7,-2],[3,-2]]],shapeType=shapefile.POLYLINE) # Membuat  kkordinat berbentuk POLYLINE



w.save("soal10")