import shapefile # memasukan module shapefile
w=shapefile.Writer()    # mendefinisikan w sebagai shapefile.writer

w.shapeType     # melakukan penerapan shapeType pada w
w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")   # membuat kolom dengan type character di dalamnya

w.record("ngek","satu") # isi dari kolom tersebut dan sebagai tempat point 1,1
w.record("ngok","dua")  # isi dari kolom tersebut dan sebagai tempat point 2,2

w.point(1,1) # membuat titik pada koordinat 1,1 dengan record ("ngek","satu") 
w.point(2,2)     # membuat titik pada koordinat 2,2 dengan record ("ngok","dua") 

w.save("cokgan") # nama untuk menyimpan file