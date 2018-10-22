import shapefile        #import modul shapefile
w=shapefile.Writer()    #deklarasi fungsi writer
w.shapeType             #apply type shape

w.field("kolom1","C")   #membuat kolom dengan tipe data character
w.field("kolom2","C")

w.record("ngek","satu") #mengisi record pada kolom yang sudah dibuat

    
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])    #membuat titik koordinat, dan membentuk sebuah polyline

w.save("soal5")     #untuk menyimpan data menjadi file shp