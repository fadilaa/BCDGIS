import shapefile            #import modul shapefile
w=shapefile.Writer()        #deklarasi fungsi writer
w.shapeType                 #apply type shape

w.field("kolom1","C")       #membuat kolom dengan tipe character
w.field("kolom2","C")

w.record("ngek","satu")     #mengisi record pada kolom yang sudah di buat
w.record("crot","dua")

w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)  #membuat koordinat dengan 2 buah persegi panjang.
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE)


w.save("soal9")             #untuk menyimpan file menjadi shp file.