def assign_students_to_sections(sections, *students):
  total_sections = len(sections)
  result_dict = {}
  for i in sections:
    result_dict[i] = []

  for student in students:
    ascii_sum = 0
    for i in student:
      ascii_sum += ord(i)
    assigned_section = ascii_sum % total_sections
    result_dict[sections[assigned_section]].append(student)

  return result_dict

print(assign_students_to_sections ('ABCDE', 'Alice',
'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'))
