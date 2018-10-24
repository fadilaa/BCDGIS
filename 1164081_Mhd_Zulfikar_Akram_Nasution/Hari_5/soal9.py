import shapefile					#mimport modul shapefile
w=shapefile.Writer()				#deklarasikan fungsi writer
w.shapeType							#apply shapetype

w.field("kolom1","C")				#membuat kolom dengan tipe data character
w.field("kolom2","C")

w.record("ngek","satu")				# mengisi record padakolom yang sudah disediakan
w.record("crot","dua")



w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)	#membuat titik koordinat yang menghasilkan bentuk persegi
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE) 	#membuat titik koordinat yang menghasilkan bentuk persegi panjang


w.save("soal9") 	#menyimpan file dalam bentuk shp file