import shapefile  # import modul shapefile
w = shapefile.Writer()  # deklarasi fungi writer
w.shapeType  # melakukan apply tipe shape

w.field("kolom1", "C")  # membuat kolom dengan tipe character
w.field("kolom2", "C")

w.record("ngek", "satu")  # isi dari record field diatas
w.record("ngok", "dua")

w.point(1, 1)  # membuat point/titik
w.point(2, 2)

w.save("soal1")  # untuk menyimpan file.
