import shapefile
w=shapefile.Writer(shapeType=1)
w.shapeType
w.shapeType=3
w.shapeType

w.field("kolom1","C")   # mendeklalasikan kolom 1 
w.field("kolom2","C")   # mendeklarasikan kolom 2

w.record("ngek","satu") # membuat rekaman ke satu sebagai tempat point 1,1
w.record("ngok","dua")  # membuat rekaman ke dua sebagai tempat point 2,2

w.point(1,1) # koordinat 1,1
w.point(2,2)  # koordinat 2,2   

w.save("cokgan2")   #ketika di run python akan menyimpan nama dengan cokro3.shp