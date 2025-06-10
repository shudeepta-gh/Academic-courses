class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()


  def __hash_function(self, key):
    sum = 0
    if(len(key) % 2 == 0):
      for i in range(0,len(key),2):
        sum += ord(key[i])

    elif(len(key) % 2 !=0):
      for i in range(1,len(key),2):
        sum += ord(key[i])

    return sum % self.length


  def insert(self, key, value):
    hash_index = self.__hash_function(key)

    if (self.ht[hash_index].value == None):
        self.ht[hash_index] = Node((key, value))
    else:
        n1 = Node((key, value))

        if self.ht[hash_index].value[1] < value:
            if self.ht[hash_index].value[0] == key:
                self.ht[hash_index].value[1]==n1.value[1]
            else:
                n1.next = self.ht[hash_index]
            self.ht[hash_index] = n1
            return

        prev = self.ht[hash_index]
        temp = self.ht[hash_index].next

        while (temp!=None):
            if temp.value[1] < value:
                prev.next = n1
                n1.next = temp
                return
            prev = temp
            temp = temp.next


        prev.next = n1



#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------------")
ht.insert("apple", 100)
ht.insert("guava", 10)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 100)-->('guava', 10) -->
# 2 ('cherry', 50)-->
