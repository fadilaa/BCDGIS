import shapefile                                   #Melakukan import modul shapefile
w=shapefile.Writer()                               #Mendeklarasikan fungsi writer
w.shapeType                                        #Apply type shape

w.field("kolom1","C")                              #Untuk membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")                            #Mengisi record pada kolom yang telah dibuat


w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])    #Membuat titik koordinat line dan akan membentuk polyline

w.save("soal5")                                    #Untuk menyimpan soal dengan bentuk shp file