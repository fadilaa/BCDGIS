import shapefile    
w=shapefile.Writer()   
w.shapeType    

w.field("kolom1","C")  
w.field("kolom2","C")   

w.record("oooooaaahhh","sada") 
w.record("uncch","dua") 
w.record("asss","tolu")  
w.record("ohhh","opat")
w.record("hachim","lima") 
w.record("ahahahaha","onom")
w.record("oooooaaahhh","pitu") 

w.poly(parts=[[[1,2],[2,3], [3,2],[2,1],[1,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,2],[6,3], [7,2],[6,1],[5,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[9,2],[10,3], [11,2],[10,1],[9,2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,6],[6,7], [7,6],[6,5],[5,6]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,10],[2,11], [3,10],[2,9],[1,10]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,10],[6,11], [7,10],[6,9],[5,10]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[9,10],[10,11], [11,10],[10,9],[9,10]]],shapeType=shapefile.POLYLINE)

w.save("soal10")