import shapefile																#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()															#Untuk memasang fungsi writer
w.shapeType																		#Untuk mengaktifkan type shape

w.field("kolom1","C")															#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")															#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada


w.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE)	#Membuat koordinat berbentuk polygon seperti 2 segitiga sama kaki saling berhadapan

w.save("soal8")																	#Untuk menyimpan file menjadi file shp dengan nama file soal8.shp
