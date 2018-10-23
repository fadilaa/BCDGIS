import shapefile	#Untuk mengimport modul shapefile
w=shapefile.Writer(shapefile.POINTM) #untuk membaca modul shapefile
w.shapeType 	#untuk apply shapeType

w.field("kolom1","C") #Membuat kolom dengan type data character
w.field("kolom2","C") #Membuat kolom dengan type data character

w.record("ngek","satu") #mengisi record pada kolom yg sudah dibuat
w.record("ngok","dua")  #mengisi record pada kolom yg sudah dibuat

w.point(1,1) #Membuat point koordinat
w.point(2,2) #Membuat point koordinat

w.save("soal4") #untuk menyimpan file dengan format shp&dbf

