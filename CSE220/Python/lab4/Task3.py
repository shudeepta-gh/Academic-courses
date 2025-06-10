class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'({head.key}, {head.value})', end = '-->')
        head = head.next
      print('None')
      idx += 1

  def __hash_function(self, key):
    hashed_index = (key+3) % len(self.ht)

    return hashed_index

  def remove(self, key):
    hashed_index = self.__hash_function(key)
    if(self.ht[hashed_index] == None):
      print("Nothing to remove")
      return
    else:
      if(self.ht[hashed_index].key == key):
        self.ht[hashed_index] = self.ht[hashed_index].next

      else:
        prev = self.ht[hashed_index]
        temp = self.ht[hashed_index].next
        while(temp != None):
          if(temp.key == key):
            prev.next = temp.next
            return
          prev = temp
          temp = temp.next

    print("The key doesn't exist")
    return



#Driver Code
arr=[(34, 'Abid') , (4, 'Rafi'), (6, 'Karim'), (3, 'Chitra'), (22, 'Nilu')]
ht = Hashtable(6)
ht.create_from_array(arr)
ht.print_hashtable()

#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(9)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')
print('======================')

ht.remove(4)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None
