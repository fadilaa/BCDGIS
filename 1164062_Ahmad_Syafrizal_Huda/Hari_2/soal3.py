import shapefile						#Untuk mengambil data modul pada shapefile
w=shapefile.Writer(shapeType=1)			#Untuk memasang fungsi writer dengan shapetypenya = 1
w.shapeType 							#Untuk mengaktifkan type shape
w.shapeType=3							#Untuk mengaktifkan type shape 3
w.shapeType 							#Untuk mengaktifkan type shape

w.field("kolom1","C")					#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")					#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada jika record terdapat 2 maka koordinatnya jga 2 bentuk
w.record("ngok","dua")

w.point(1,1)							#Membuat koordinat berbentuk garis namun tidak terlihat	
w.point(2,2)

w.save("soal3")							#Untuk menyimpan file menjadi file shp dengan nama file soal3.shp