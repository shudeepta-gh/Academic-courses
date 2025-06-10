def task1A():
    count = 1
    while(count<=10):
      print(count,end=" ")
      count+=1
def task1B_recursive(n):
   count=n
   if(count>10):
      return
   print(count,end=" ")
   task1B_recursive(count+1)


def task1C(start,stop):
   while(start<=stop):
      print(start,end=" ")
      start+=1

def task1D_recursive(start,stop):
  if(start>stop):
    return
  print(start,end=" ")
  task1D_recursive(start+1,stop)

task1A()
print()
task1B_recursive(1)
print()
N=int(input("Enter a number:"))
task1C(1,N)
print()
N=int(input("Enter a number:"))
task1D_recursive(1,N)
