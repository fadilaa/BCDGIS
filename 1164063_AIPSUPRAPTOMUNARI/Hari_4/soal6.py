import shapefile					#untuk mengambil data modul pada shapefile
w=shapefile.Writer()				#memasang fungsi writer
w.shapeType							#untuk mengaktifkan type shape

w.field("kolom1","C")				#untuk membuat kolom dengan menggunakan type data char			
w.field("kolom2","C")

w.record("ngek","satu")				#kolom yang dibuat akan diisikan recordnya sesuaid dengan kolom yang ada


w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE)		#membuat koordinat berbentuk polyline seperti garis lurus horizontal (mendatar)

w.save("soal6")													#untuk menyimpan file menjadi shp 