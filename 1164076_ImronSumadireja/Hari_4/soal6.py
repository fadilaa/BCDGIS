import shapefile            #import modul shapefile
w = shapefile.Writer()      #deklarasi fungsi writer
w.shapeType                 #apply type shape

w.field("kolom1", "C")      #membuat kolom dengan tipe data character
w.field("kolom2", "C")

w.record("ngek", "satu")    #mengisi record pada kolom yang sudah di buat


w.poly(parts=[[[1, 3], [5, 3]]], shapeType=shapefile.POLYLINE)  #membuat titik koordinat dan membentuk sebuah polyline dengan menambahkan deklarasi shapetype POLYLINE

w.save("soal6") #untuk menyimpan file data menjadi shp file