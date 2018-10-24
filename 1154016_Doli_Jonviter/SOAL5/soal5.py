import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menggunakan tipe apa shape di buat
w.field("kolom1","C") #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat file dengan nama kolom 2 dengan type character
w.record("ngek","satu")
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #memberikan koordinat untuk membuat line
w.save("soal5") #menyimpan file shape dengan nama soal5
