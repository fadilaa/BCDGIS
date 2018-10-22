import shapefile                           #import modul shapeFile
w=shapefile.Writer(shapefile.POINTM)       #deklarasi fungsi writer dengan parameter point
w.shapeType                                #apply type shape

w.field("kolom1","C")                   #membuat kolom dengan tipe data character
w.field("kolom2","C")
        
w.record("ngek","satu")                 #mengisi record pada kolom yang sudah dibuat
w.record("ngok","dua")

w.point(1,1)                            #membuat titik/point koordinat
w.point(2,2)

w.save("soal4")                         #untuk menyimpan file menjadi shp file