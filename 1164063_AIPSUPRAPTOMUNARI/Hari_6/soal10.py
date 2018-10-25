import shapefile					#untuk mengambil data modul pada shapefile
w=shapefile.Writer()				#untuk memasang fungsi writer
w.shapeType							#untuk mengaktifkan type shape

w.field("kolom1","C")				#untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("gskuy","ghola")			#kolom yang dibuat aka diisikan recordnya sesuai dengan kolom yang ada pada setiap ruang dengan nama unik dan lucu karena recordnya ada 6 maka bentuk koordinat juga ada 6
w.record("gcaw","gwhicis")
w.record("gkuy","gliving")
w.record("gwoles","gcapcus")
w.record("gkerad","gkalem")
w.record("gsantuy","gtayo")



w.poly(parts=[[[1,1],[4,1],[1,3],[1,1]]],shapeType=shapefile.POLYLINE)	#membuat koordinat berbemtuk pplygon seperti 6 buah segita siku-siku membentuk persegi panjang dengan nama gskuy
w.poly(parts=[[[4,1],[1,3],[4,3],[4,1]]],shapeType=shapefile.POLYLINE)	#gcaw
w.poly(parts=[[[1,3],[1,5],[4,3],[1,3]]],shapeType=shapefile.POLYLINE)	#gkuy
w.poly(parts=[[[4,3],[4,5],[1,5],[4,3]]],shapeType=shapefile.POLYLINE)	#gwoles
w.poly(parts=[[[1,7],[1,5],[4,5],[1,7]]],shapeType=shapefile.POLYLINE)	#gkerad
w.poly(parts=[[[4,5],[4,7],[1,7],[4,5]]],shapeType=shapefile.POLYLINE)	#gsantuy


w.save("soal10")														#untuk menyimpan file menjadi file shp dengan nama file soal10.shp