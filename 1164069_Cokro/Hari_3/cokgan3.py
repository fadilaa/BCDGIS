import shapefile    
w=shapefile.Writer(shapefile.POINTM) # mendekralasikan bentuk point atau titik
w.shapeType # w di deklalasikan dalam bentuk tipe shape

w.field("kolom1","C")   # mendeklalasikan kolom 1 
w.field("kolom2","C")   # mendeklarasikan kolom 2

w.record("ngek","satu") # membuat rekaman ke satu sebagai tempat point 1,1
w.record("ngok","dua")  # membuat rekaman ke dua sebagai tempat point 2,2

w.point(1,1)    # koordinat 1,1
w.point(2,2)    # koordinat 2,2

w.save("cokgan3")   #ketika di run python akan menyimpan nama dengan cokro3.shp