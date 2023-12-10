def f(tab2d):
    p1 = tab2d[0][0]+tab2d[0][1]+tab2d[0][2]
    p12 = tab2d[0][0]+tab2d[1][0]+tab2d[2][0]
    p2 = tab2d[1][0]+tab2d[1][1]+tab2d[1][2]
    p22 = tab2d[0][1]+tab2d[1][1]+tab2d[2][1]
    p3 = tab2d[2][0]+tab2d[2][1]+tab2d[2][2]
    p32 = tab2d[0][2]+tab2d[1][2]+tab2d[2][2]
    
    if p1 == p12 and p2 == p22 and p3 == p32:
        return True
    else:
        return False
    

print(f([[3,7,2],[4,2,5],[9,2,1]]))