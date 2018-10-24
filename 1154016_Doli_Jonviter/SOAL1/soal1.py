import shapefile #mengimport shapefile pyshp
w=shapefile.Writer() #membuat file baru
w.shapeType #mengecek type

w.field("kolom1","C") #membuat field dbs yang memiliki type karakter
w.field("kolom2","C") #membuat field dbs yang memiliki type karakter

w.record("ngek","satu")#isi dari kolom
w.record("ngok","dua") #isi dari kolom

w.point(1,1) #mengisi shp dengan titik poin yaitu y,x
w.point(2,2) #mengisi shp dengan titik poin yaitu y,x

#jika recordnya ada 2 maka pointnya juga harus 2 tidak boleh 1 atau lebih sesuai dengan jumlah record yang ada 

w.save("soal1")#save file. Dimana nama filenya soal1. berikutnya akan keluar 2 file di folder yang sama