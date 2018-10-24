import shapefile                                                                #mengimport modul shapefile
w=shapefile.Writer()                                                            #mendeklarasikan fungsi writer
w.shapeType                                                                     #meng apply type shape

w.field("kolom1","C")                                                           #membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")                                                         #mengisi record pada sebuah kolom yang sudah disiapkan


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE)   #membuat koordinat polyline yang hasilnya akan membentuk polygon karena setiap garis akan saling berhubungan

w.save("soal8")                                                                 #untuk menyimpan file data dengan bentuk shp file