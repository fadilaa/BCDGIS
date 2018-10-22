import shapefile#mengimport shapefile pyshp
w=shapefile.Writer(shapeType=1)#membuat file baru dengan type
w.shapeType  #mengecek type

w.shapeType=3
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C") 

w.record("ngek","satu")
w.record("ngok","dua")

w.point(1,1)
w.point(2,2)

w.save("soal3") 