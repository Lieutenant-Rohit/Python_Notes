#2D List

fruits = ["apple", "banana", "orange"]
vegetables = ["Celery","Carrots","Potatoes"]
meat = ["Chicken","fish","Turkey"]

grocery = [fruits, vegetables, meat]
# print(grocery[0])
# print(grocery[1])
# print(grocery[2])
# print(grocery[0][0])

for collection in grocery:
  for item in collection:
      print(item,end=" ")
  print()


##Making a Dial Paid using tuple Booz its ordered and unchangeable and faster than list
numpad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for item in numpad:
    for x in item:
        print(x,end="    ")
    print()