import shapefile                                                                #mengimport modul shapefile
w=shapefile.Writer()                                                            #mendeklarasikan fungsi writer
w.shapeType                                                                     #meng apply type shape

w.field("kolom1","C")                                                           #membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")                                                         #mengisi record pada sebuah kolom yang sudah disiapkan
w.record("crot","dua")



w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)  #membuat koordinat dan menghasilkan bentuk 1 persegi dan 1 persegi panjang
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE)


w.save("soal9")                                                                 #untuk menyimpan file data dengan bentuk shp file