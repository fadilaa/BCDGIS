import shapefile #mengimpor modul shapefile
w=shapefile.Writer(shapeType=1) #Instansiasi writer method
w.shapeType #Shapetype adalah standar nomor jenis data geometri oleh ESRI
w.field("kolom1","C") #Membuat atribut kolom1 type data character dahulu kemudian menambahkan record.
w.field("kolom2","C") #Membuat atribut kolom2 dengan type data character dahulu kemudian menambahkan record.
w.record("ngek","satu") #membuat record dengan nama ngek, dengan type isi kolom2 adalah satu
w.record("ngok","dua") #membuat record dengan nama ngek, dengan type isi kolom2 adalah satu
#Untuk menambahkan record tergantung dengan type ESRInya.

w.point(1,1)  #w.point (x,y)
w.point(2,2) #w.point (x,y)
w.save("soal2") #menyimpan file yang sudah di buat