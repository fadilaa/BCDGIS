import shapefile																#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()															#Untuk memasang fungsi writer
w.shapeType																		#Untuk mengaktifkan type shape

w.field("kolom1","C")															#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")															#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada jika record ada 2 maka pada koordinatnya jga ada 2 bentuk
w.record("ngok","dua")



w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)	#Membuat koordinat berbentuk polygon seperti 2 persegi panjang 1 besar dan satu yang kecil
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE)


w.save("soal9")																	#Untuk menyimpan file menjadi file shp dengan nama file soal9.shp
