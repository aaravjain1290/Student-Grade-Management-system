number_of_students=int(input("Enter the number of students you would like to enter: "))

student_subject_grades={}

for students in range(number_of_students):
  
  grades=[]
  
  student_name=input("Enter students name: ")

  subject_grades1=int(input("Enter subject grades: "))
  if subject_grades1 <0 or subject_grades1 >100:
   print("Error, score is not possible")
  else:
    grades.append(subject_grades1)

  subject_grades2=int(input("Enter subject grades: "))
  if subject_grades2 <0 or subject_grades2 >100:
   print("Error, score is not possible")
  else:
    grades.append(subject_grades2)

  subject_grades3=int(input("Enter subject grades: "))
  if subject_grades3 <0 or subject_grades3 >100:
   print("Error, score is not possible")
  else:
    grades.append(subject_grades3)

  student_subject_grades[student_name]=grades

print(student_subject_grades['aarav'])

#Functions:

students_added_counter=0

def add_student(name, grade1, grade2, grade3):
  global students_added_counter
  grades_function=[grade1, grade2, grade3]
  student_subject_grades[name]=grades_function
  students_added_counter +=1
  print("Student appended succesfully!")


def calc_student_average(name):
  grades= student_subject_grades[name]
  total=0
  for i in grades:
    total +=i
  return total/len(grades)


def grade_converter(average):
  if average>=90:
    return "A"
  elif average>=80 and average<=89:
    return "B"
  elif average>=70 and average<=79:
    return "C"
  elif average>=60 and average<=69:
    return "D"
  else:
    return "F"


def display_students(name):
  grades=student_subject_grades[name]
  avg=calc_student_average(name)
  letter=grade_converter(avg)

  print(f"Name: {name}")
  print(f"Grades: {grades}")
  print(f"Average: {avg}")
  print(f"Letter grade: {letter}")

def get_highest_avg():
  all_averages=[]
  names=[]
  for student in student_subject_grades:
    avg=calc_student_average(student)
    all_averages.append(avg)
    names.append(student)
  
  highest_avg=max(all_averages)
  top_student_index = all_averages.index(highest_avg)
  top_student = names[top_student_index]
  
  print(f"Top Student: {top_student} with an average of {highest_avg}")

import statistics

def calculate_class_average():
  all_student_averages=[]
  for student in student_subject_grades:
    avg = calc_student_average(student)
    all_student_averages.append(avg)
  
  if all_student_averages:
    class_avg = statistics.mean(all_student_averages)
    print(f"The class average is: {class_avg}")
  else:
    print("No student data available to calculate class average")

#Calling functions:
add_student("bob", 89, 97, 76)
print(student_subject_grades)

average=calc_student_average("aarav")
print(student_subject_grades)
print(average)

grade_converter(average)

display_students("alice")

get_highest_avg()

calculate_class_average()

#Summary/report:

print("-"*50)
print("                    SUMMARY:")
total_students= number_of_students + students_added_counter
print(f"Number of students: {total_students}")
print(calculate_class_average())
print(get_highest_avg())

failing_students=0
passing_students=0

for students in student_subject_grades:
  avg=calc_student_average(students)
  if avg<50:
    failing_students +=1
  else:
    passing_students +=1

print(f"Number of passing students: {passing_students}")
print(f"Number of failing students: {failing_students}")

percentage_of_passing_students=((passing_students)/total_students)*100
percentage_of_failing_students=((failing_students)/total_students)*100

print(f"Percentage of passing students: {percentage_of_passing_students}%")
print(f"Percentage of failing students: {percentage_of_failing_students}%")