import shapefile                                                                #mengimport modul shapefile
w=shapefile.Writer()                                                            #mendeklarasikan fungsi writer
w.shapeType                                                                     #meng apply type shape

w.field("kolom1","C")                                                           #membuat kolom dengan menggunakan tipe data character
w.field("kolom2","C")

w.record("segitiga","bertua")                                                   #mengisi record pada kolom yang telah disediakan
w.record("segitiga","beradik")
w.record("segitiga","berkaka")
w.record("segitiga","berpapah")
w.record("segitiga","bermamah")
w.record("segitiga","berduda")
w.record("segitiga","berjanda")
w.record("segitiga","beranak")

w.poly(parts=[[[-1,1],[0,3],[1,1],[-1,1]]],shapeType=shapefile.POLYLINE)        #membuat koordinat polygon yang menghasilkan 8 bentuk segitiga sama kaki
w.poly(parts=[[[-1,5],[0,3],[1,5],[-1,5]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[2,2],[0,3],[2,4],[2,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-2,2],[0,3],[-2,4],[-2,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-2,2],[-4,3],[-2,4],[-2,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-3,1],[-4,3],[-5,1],[-3,1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-6,2],[-4,3],[-6,4],[-6,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-3,5],[-4,3],[-5,5],[-3,5]]],shapeType=shapefile.POLYLINE)

w.save("soal10")                                                                #untuk menyimpan file data dengan bentuk shp file