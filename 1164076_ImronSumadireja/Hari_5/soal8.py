import shapefile            #import modul shapefile
w=shapefile.Writer()        #deklarasi fungsi writer
w.shapeType                 #apply type shape

w.field("kolom1","C")       #membuat kolom dengan type character
w.field("kolom2","C")

w.record("ngek","satu")     #mengisi record pada kolom yang sudah di buat


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE)   #membentuk koordniat polygone dengan membentuk 2 segitiga sama kaki yang saling berhadapan

w.save("soal8")             #untuk menyimpan file menjadi shp file