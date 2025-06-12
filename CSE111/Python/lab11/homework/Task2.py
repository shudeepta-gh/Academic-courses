class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam(Exam):
  def __init__(self,marks,time,*subjects):
    super().__init__(marks)
    self.time=time
    self.subjects=list(subjects)


  def __str__(self):
    self.subject=""
    self.count=2
    for subject in self.subjects:
      if subject!=self.subjects[-1]:
        self.subject+=f" {subject},"

      else:
        self.subject+=f" {subject}"

      self.count+=1
    return f"Marks: {self.marks} Time:{self.time} minutes Number of Parts: {self.count}"


  def examSyllabus(self):

    return f"{super().examSyllabus()},{self.subject}"

  def examParts(self):
    self.part=2
    self.parts=""

    for subject in self.subjects:
      self.part+=1
      self.parts+=f"Part: {self.part} - {subject} \n"

    return f"{super().examParts()}{self.parts}"


engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())
