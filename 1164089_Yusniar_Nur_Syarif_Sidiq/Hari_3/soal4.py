import shapefile                        #Untuk mengimport modul shapefile
w=shapefile.Writer(shapefile.POINTM)    #Untuk mendeklarasi fungsi writer dengan parameter point
w.shapeType                             #Untuk apply type shape

w.field("kolom1","C")                   #Untuk membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")                 #Kolom yang dibuat akan diisikan Recordnya
w.record("ngok","dua")

w.point(1,1)                            #Membuat Point Koordinat
w.point(2,2)

w.save("soal4")                         #Untuk menyimoan file tersebut menjadi shp file