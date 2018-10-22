import shapefile										#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()									#Untuk memasang fungsi writer
w.shapeType												#Untuk mengaktifkan type shape

w.field("kolom1","C")									#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")									#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada


w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])			#Membuat koordinat berbentuk line/garis

w.save("soal5")											#Untuk menyimpan file menjadi file shp pada soal5