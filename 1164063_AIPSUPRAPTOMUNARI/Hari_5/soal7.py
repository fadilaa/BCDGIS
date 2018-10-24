import shapefile					#mengimportkan modul shapefile 
w=shapefile.Writer()				#mendeklarasikan fungsi writer
w.shapeType							#meng-apply type shape

w.field("kolom1","C")				#membuat kolom dengan menggunakan tipe data karakter
w.field("kolom2","C")

w.record("ngek","satu")				#mengisi record pada sebuah kolom yang sudah disiapkan


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE)		#merupakan koordinat yang nantinya akan menjadi garis polyline

w.save("soal7")																#untuk menyimpan file data dengan bentuk shp file