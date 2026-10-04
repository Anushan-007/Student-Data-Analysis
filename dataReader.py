import pandas as pd
import matplotlib.pyplot as plt

studentData =  pd.read_csv("Book1.csv")



studentData = studentData.to_dict()
studentData = studentData.to_dict(orient="records")

for student in studentData:
    if student['name'] == 'Asha':
        student['age'] = 25


for student in studentData:
    if student['name'] == 'Kumar':
        student['course'] = 'LAW'


newStudent = {
    'name': 'Anushan',
    'age': 24,
    'course': 'IT'
}

studentData.append(newStudent)
print(studentData)


studentData.pop(1)
print(studentData)


studentData.pop(0)
print(studentData)

studentData.remove(newStudent)



print(studentData)


x = studentData["name"]
y = studentData["marks"]

plt.bar(x,y)
plt.show()  