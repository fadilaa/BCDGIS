import shapefile 
w=shapefile.Writer() 
w.shapeType 
w.field("kolom1","C") 
w.field("kolom2","C")


w.record("kotak","satu")
w.record("kotak","dua")
w.record("kotak","tiga")
w.record("kotak","empat")
w.record("kotak","lima")
w.record("kotak","enam")
w.record("kotak","tujuh")
 
w.poly(parts=[[[1,3],[2,3], [2,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE) 
w.poly(parts=[[[3,5],[4,5], [4,4],[3,4], [3,5]]],shapeType=shapefile.POLYLINE) 
w.poly(parts=[[[-1,1],[0,1], [0,0],[-1,0], [-1,1]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[3,1],[3,2], [2,2],[2,1], [3,1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,3],[5,4], [4,4],[4,3], [5,3]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,-1],[1,0], [0,0],[0,-1], [1,-1]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[-1,3],[-2,3], [-2,2],[-1,2], [-1,3]]],shapeType=shapefile.POLYLINE)
 
w.save("soal10")