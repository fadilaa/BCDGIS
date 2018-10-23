import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C") # nama nama kolom
w.field("kolom2","C")   # nama kolom

w.record("ngek","satu") # nama record nya ngek dan satu 

w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # menterjemahkan titik koordinat ujung ujung dari setiap garis
w.save("cokgan4") # di simpan dalam bentuk shp dengan nama cokgan4