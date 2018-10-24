import shapefile                    #mengimport modul shapefile
w=shapefile.Writer(shapeType=1)     #mendeklarasikan fungsi writer dan menambahkan parameter shapetype
w.shapeType                         #meng apply type shape
w.shapeType=3                       #merubah type shape
w.shapeType                         #apply type shape

w.field("kolom1","C")               #membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")             #mengisi record pada sebuah kolom yang sudah disiapkan
w.record("ngok","dua")

w.point(1,1)                        #membuat point dengan koordinat 1 pada sumbu x dan 1 pada sumbu y
w.point(2,2)                        #membuat point dengan koordinat 2 pada sumbu x dan 2 pada sumbu y

w.save("soal3")                     #untuk menyimpan file data dengan bentuk shp file