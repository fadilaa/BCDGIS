import shapefile 		# mengimport modul shapefile
w=shapefile.Writer()	#mendeklarasikan fungsi writer
w.shapeType 			#meng apply shapetype

w.field("kolom1","C") 	#membuat kolom dengan tipe character
w.field("kolom2","C")

w.record("ngek","satu")	#mengisi record atau data pada kolom yang sudah disediakan


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE)	#membuat titik koordinat polyline yang hasilnya menjadi sebuah polygone karena titik awal bertemu dengan titik akhir

w.save("soal8")		#untuk menyimmpan data dalam bentuk shp file