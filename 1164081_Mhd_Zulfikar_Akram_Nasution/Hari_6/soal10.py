import shapefile					#mimport modul shapefile
w=shapefile.Writer()				#deklarasikan fungsi writer
w.shapeType							#apply shapetype

w.field("kolom1","C")				#membuat kolom dengan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")				# mengisi record padakolom yang sudah disediakan
w.record("crot","dua")
w.record("crot","tiga")
w.record("crot","empat")
w.record("crot","lima")
w.record("crot","enam")
w.record("crot","tujuh")
w.record("crot","delapan")

w.poly(parts=[[[-1.5,1],[0,3.5], [1.5,1],[-1.5,1]]],shapeType=shapefile.POLYLINE)	#membuat titik koordinat yang menghasilkan bentuk persegi
w.poly(parts=[[[-1.5,3.5],[0,6], [1.5,3.5],[-1.5,3.5]]],shapeType=shapefile.POLYLINE)	#membuat titik koordinat yang menghasilkan bentuk persegi panjang
w.poly(parts=[[[-1.5,6],[0,8.5], [1.5,6],[-1.5,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1.5,8.5],[0,11], [1.5,8.5],[-1.5,8.5]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1.5,11],[0,13.5], [1.5,11],[-1.5,11]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1.5,13.5],[0,16], [1.5,13.5],[-1.5,13.5]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1.5,16],[0,18.5], [1.5,16],[-1.5,16]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1.5,18.5],[0,21], [1.5,18.5],[-1.5,18.5]]],shapeType=shapefile.POLYLINE)
w.save("soal10") 	#menyimpan file dalam bentuk shp file