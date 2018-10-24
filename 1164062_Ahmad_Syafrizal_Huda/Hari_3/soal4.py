import shapefile                        #Untuk mengambil data modul pada shapefile
w=shapefile.Writer(shapefile.POINTM)    #Untuk memasang fungsi writer dengan parameter point
w.shapeType                             #Untuk mengaktifkan type shape

w.field("kolom1","C")                   #Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")                 #Kolom yang dibuat akan diisikan Recordnya 
w.record("ngok","dua")

w.point(1,1)                            #Membuat koordinat berbentuk point/titik
w.point(2,2)

w.save("soal4")                         #Untuk menyimpan file menjadi file shp dengan nama file soal4.shp
