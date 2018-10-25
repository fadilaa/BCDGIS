import shapefile    # memasukan module shapefile
w=shapefile.Writer()    # mendefinisikan w sebagai shapefile.writer
w.shapeType     # melakukan penerapan shapeType pada w

w.field("kolom1","C") # membuat kolom dengan type character di dalamnya
w.field("kolom2","C") # membuat kolom dengan type character di dalamnya

w.record("ngek","satu") # membuat rekaman ke satu sebagai tempat semua titik koordianat

w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # menterjemahkan titik koordinat ujung ujung dari setiap garis
w.save("cokgan4") # di simpan dalam bentuk shp dengan nama cokgan4