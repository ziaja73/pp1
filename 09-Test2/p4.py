def f(py: dict):
    for x, y in py.items():
        count = 0
        for ocena in y:
            count += ocena
        py.update({x:count/len(y)})
    posortowany_slownik = sorted(py.items(), key=lambda x: x[1], reverse=True)
    return posortowany_slownik[0][0]
    
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))