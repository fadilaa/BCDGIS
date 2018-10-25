import shapefile     # memasukan module shapefile
w=shapefile.Writer(shapeType=1)      # mendefinisikan w sebagai shapefile.writer dengan shape type 1
w.shapeType     # melakukan penerapan shapeType pada w
w.shapeType=3   # melakukan penerapan shapeType pada w sehingga berbentuk garis
w.shapeType     # melakukan penerapan shapeType pada w dari shapeType=3

w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")   # membuat kolom dengan type character di dalamnya

w.record("ngek","satu") # isi dari kolom tersebut dan sebagai tempat point 1,1
w.record("ngok","dua")  # isi dari kolom tersebut dan sebagai tempat point 2,2

w.point(1,1) # membuat titik pada koordinat 1,1 dengan record ("ngek","satu") 
w.point(2,2)  # membuat titik pada koordinat 2,2 dengan record ("ngok","dua")
                #sehinggga keduanya menjadi suatu garis

w.save("cokgan2")   #ketika di run python akan menyimpan nama dengan cokro2.shp