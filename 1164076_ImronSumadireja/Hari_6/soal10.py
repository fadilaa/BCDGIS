import shapefile            #import modul shapefile
w=shapefile.Writer()        #deklarasi fungsi writer
w.shapeType                 #apply type shape

w.field("kolom1","C")       #membuat kolom dengan type character
w.field("kolom2","C")

w.record("jajargenjang","kuat")     #mengisi record pada kolom yang sudah di buat
w.record("jajargenjang","ashiap")
w.record("jajargenjang","merdeka")
w.record("jajargenjang", "es en i")
w.record("jajargenjang","united")
w.record("jajargenjang","islan")
w.record("jajargenjang", "ocean")

w.poly(parts=[[[1,1],[2,3],[5,3],[4,1],[1,1]]], shapeType=shapefile.POLYLINE)   #membentuk koordniat polygone dengan membentuk 7 buah jajargenjang
w.poly(parts=[[[4,1],[5,3],[8,3],[7,1],[1,1]]], shapeType=shapefile.POLYLINE)
w.poly(parts=[[[7,1],[8,3],[11,3],[10,1],[1,1]]], shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,-1],[2,-3],[5,-3],[4,-1],[1,-1]]], shapeType=shapefile.POLYLINE)
w.poly(parts=[[[4,-1],[5,-3],[8,-3],[7,-1],[1,-1]]], shapeType=shapefile.POLYLINE)
w.poly(parts=[[[7,-1],[8,-3],[11,-3],[10,-1],[1,-1]]], shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1,1],[-2,3],[-5,3],[-4,1],[-1,1]]], shapeType=shapefile.POLYLINE)

w.save("soal10")             #untuk menyimpan file menjadi shp file