import shapefile        #import modul shapefile
w=shapefile.Writer()    #deklarasi fungsi writer
w.shapeType             #apply type shape

w.field("kolom1","C")   #membuat kolom dengan tipe character
w.field("kolom2","C")

w.record("ngek","satu") #mengisi record pada kolom yang sudah di buat


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE)      #memebuat titik koordinat bentuk polyline dengan menambahkan deklarasi shapetype polyline

w.save("soal7")         #untuk menyimpan file menjadi shp file