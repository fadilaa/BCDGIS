import shapefile						# untuk mengimpor modul shapefile
w=shapefile.Writer()					# membaca modul shapefile
w.shapeType								# untuk menerima shapeType

w.field("kolom1","C")					# membuat kolom dengan tipe data karakter
w.field("kolom2","C")					

w.record("ngek","satu")					# mengisi record pada kolom yang dibuat


w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat titik koordinat line dan akan membentuk polyline

w.save("soal5")							# menyimpan file dengan format shp