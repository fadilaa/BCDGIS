import shapefile    # memasukan module shapefile
w=shapefile.Writer(shapefile.POINTM) # mendekralasikan bentuk point atau titik
w.shapeType # w di deklalasikan dalam bentuk tipe shape

w.field("kolom1","C")   # membuat kolom dengan type character di dalamnya
w.field("kolom2","C")   # membuat kolom dengan type character di dalamnya

w.record("ngek","satu") # membuat rekaman ke satu sebagai tempat point 1,1
w.record("ngok","dua")  # membuat rekaman ke dua sebagai tempat point 2,2

w.point(1,1)    # membuat titik pada koordinat 1,1 dengan record ("ngek","satu")
w.point(2,2)    # membuat titik pada koordinat 2,2 dengan record ("ngok","dua")

w.save("cokgan3")   #ketika di run python akan menyimpan nama dengan cokro3.shp