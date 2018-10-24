import shapefile										#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()									#Untuk memasang fungsi writer
w.shapeType												#Untuk mengaktifkan type shape

w.field("kolom1","C")									#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("ngek","satu")									#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada jika record terdapat 2 maka koordinatnya jga 2 bentuk
w.record("ngok","dua")

w.point(1,1)											#Membuat koordinat berbentuk 2 point/titik warna abu-abu
w.point(2,2)

w.save("soal1")											#Untuk menyimpan file menjadi file shp dengan nama file soal1.shp