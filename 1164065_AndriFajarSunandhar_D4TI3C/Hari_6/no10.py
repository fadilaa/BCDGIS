import shapefile   #mengimport modul shapefile
w=shapefile.Writer()    #mendeklarasikan fungsi writer
w.shapeType   #meng apply type shape

w.field("Nama","C") #membuat kolom Nama dengan menggunakan tipe data character
w.field("Bentuk","C")#membuat kolom Fungsi dengan menggunakan tipe data character

w.record("sule","Segitiga") #mengisi record pada kolom yang telah disediakan
w.record("dono","Segitiga") #mengisi record pada kolom yang telah disediakan
w.record("dadang","Segitiga") #mengisi record pada kolom yang telah disediakan
w.record("diding","Segitiga") #mengisi record pada kolom yang telah disediakan
w.record("dudung","Segitiga") #mengisi record pada kolom yang telah disediakan
w.record("patrik","Segitiga")#mengisi record pada kolom yang telah disediakan


w.poly(parts=[[[-1.5,1],[0,3.5],[1.5,1],[-1.5,1]]],shapeType=shapefile.POLYLINE) #membuat koordinat polygon yang menghasilkan 6 segitiga sama kaki dengan nama sule
w.poly(parts=[[[1.5,1],[4.5,1],[3,3.5],[1.5,1]]],shapeType=shapefile.POLYLINE)  #dono
w.poly(parts=[[[-4.5,1],[-3,3.5],[-1.5,1],[-4.5,1]]],shapeType=shapefile.POLYLINE)  #dadang
w.poly(parts=[[[-3,3.5],[-1.5,6],[0,3.5],[-3,3.5]]],shapeType=shapefile.POLYLINE)  #diding
w.poly(parts=[[[3,3.5],[1.5,6],[0,3.5],[3,3.5]]],shapeType=shapefile.POLYLINE)  #dudung
w.poly(parts=[[[-1.5,6],[0,8.5],[1.5,6],[-1.5,6]]],shapeType=shapefile.POLYLINE) #patrik


w.save("soal10")     #untuk menyimpan file data dengan bentuk shp file

