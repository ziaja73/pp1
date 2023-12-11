def f(y, c):
    import json
    count = 0
    with open('09-Test2\\mock\\data.json') as file:
        details = json.loads(file.read())
        for j in details:
            if j.get('age') >= y:
                studies = j.get('studies')
                courses = studies.get('courses')
                for i in courses:
                    if i.get('name') == c:
                        grades = i.get('grades')
                        suma = sum(grades)
                        srednia = suma/len(grades)
                        if srednia >= 4:
                            count += 1
        return count

                    

print(f(21,"statistics"))