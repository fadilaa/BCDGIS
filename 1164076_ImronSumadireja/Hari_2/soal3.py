import shapefile                    #import modul shapefile
w=shapefile.Writer(shapeType=1)     #deklarasi fungsi writer dan menambahkan parameter shapeType
w.shapeType                         #melakukan apply tipe shape
w.shapeType=3                       #merubah type shape
w.shapeType                         #apply tipe shape

w.field("kolom1","C")               #membuat kolom dengan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")             #mengisi record pada kolom yang sudah dibuat
w.record("ngok","dua")

w.point(1,1)                        #membuat titik/point   
w.point(2,2)

w.save("soal3")                     #untuk menyimpan file