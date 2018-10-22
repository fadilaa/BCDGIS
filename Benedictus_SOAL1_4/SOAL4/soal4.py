import shapefile #mengimpor file shape pada python
w=shapefile.Writer(shapefile.POINTM) #mensetting file dengan jenis point
w.shapeType #menggunakan shape jenis apa

w.field("kolom1","C") #membuat atribut dengan nama kolom1 dengan type character
w.field("kolom2","C") #membuat atribut dengan nama kolom1 dengan type character

w.record("ngek","satu") #membuat record dengan isi ngek dan satu
w.record("ngok","dua") #membuat record dengan isi ngok dan dua

w.point(1,1) #membuat koordinat dengan point
w.point(2,2) #membuat koordinat dengan jenis point

w.save("soal4") #menyimpan data dengan nama soal4