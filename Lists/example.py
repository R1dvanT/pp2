#1 
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#6
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#7
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#8
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#11
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#12
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#14
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#15
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#16
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#17
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#18
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#19
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#20
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#21
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#22
thislist = ["apple", "banana", "cherry"]
del thislist
#23
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#24
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#25 
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#26
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#27
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#28
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#29
newlist = [x for x in fruits if x != "apple"]
#30
newlist = [x for x in range(10) if x < 5]
#31
newlist = [x.upper() for x in fruits] #менет все значения в масивее 
#32 
newlist = [x if x != "banana" else "orange" for x in fruits]
#33
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#34 
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#35 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#36
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#37
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#38
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#39
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#40
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)




