subjects = {
'math': {'George': 85, 'Salome': 78, 'David': 92},
'physics': {'George': 90, 'David': 75, 'Salome': 88},
'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

students = {}
for subject, scores in subjects.items():
    for name, grade in scores.items():


        if name not in students: #vamowmeb aris tu ara saxeli axal leqsikonshi
            students[name] = {}
        students[name][subject] = grade



#cal-calke xazze ver davbechde :)
print(students)