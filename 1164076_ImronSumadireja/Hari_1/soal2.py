import shapefile                    #import modul shapefile  
w=shapefile.Writer(shapeType=1)     #deklarasi fungsi writer dan menambahkan parameter shapetype
w.shapeType                         #melakukan apply tipe shape

w.field("kolom1","C")               #membuat kolom dengan tipe character
w.field("kolom2","C")

w.record("ngek","satu")             #mengisi record pada kolom yang sudah dibuat
w.record("ngok","dua")

w.point(1,1)                        #membuat point/titik   
w.point(2,2)

w.save("soal2")                     #menyimpan file