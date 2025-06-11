def username_generator(first_name,last_name,student_id,middle_name=""):

  final_result=""
  if len(first_name)<3:
    final_result+=first_name.upper()
  else:
    final_result+=first_name.upper()[0:3:1]

  final_result+=middle_name

  if len(last_name)<3:
    final_result+=last_name.lower()
  else:
    final_result+=last_name.lower()[-3:len(last_name):1]

  final_result+="_"+str(student_id)[-4:len(str(student_id)):1]



  return final_result


first_name, middle_name, last_name, student_id= input ("First Name:"), input("Middle Name:"), input ("Last Name:"), int (input ("Student ID:"))

print(username_generator (first_name, last_name, student_id))
print(username_generator(first_name, last_name, student_id, middle_name))
