import shapefile																#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()															#Untuk memasang fungsi writer
w.shapeType																		#Untuk mengaktifkan type shape

w.field("Nama","C")																#Untuk membuat kolom dengan menggunakan type data char
w.field("Fungsi","C")

w.record("TraDatar","Penopang")													#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada pada setiap ruang dengan nama yang unik dan lucu karena recordnya ada 6 maka bentuk koordinatnya jga ada 6
w.record("TraBalik","Pemberani")
w.record("TraBasi","Pembuang")
w.record("TraMiris","Pengecut")
w.record("TraPung","Pemancar")
w.record("TraFosil","Penutup")

w.poly(parts=[[[1,1],[2,2],[4,2],[5,1],[1,1]]],shapeType=shapefile.POLYLINE)	#Membuat koordinat berbentuk polygon seperti 6 buah trapesium membentuk angka 3 bangun ini saya nama kan TraDatar
w.poly(parts=[[[5,5],[4,4],[2,4],[1,5],[5,5]]],shapeType=shapefile.POLYLINE)	#TraBalik
w.poly(parts=[[[1,5],[2,6],[4,6],[5,5],[1,5]]],shapeType=shapefile.POLYLINE)	#TraBasi
w.poly(parts=[[[5,1],[4,2],[4,4],[5,5],[5,1]]],shapeType=shapefile.POLYLINE)	#TraMiris
w.poly(parts=[[[5,5],[4,6],[4,8],[5,9],[5,5]]],shapeType=shapefile.POLYLINE)	#TraPung
w.poly(parts=[[[5,9],[4,8],[2,8],[1,9],[5,9]]],shapeType=shapefile.POLYLINE)	#TraFosil

w.save("soal10")																#Untuk menyimpan file menjadi file shp dengan nama file soal10.shp