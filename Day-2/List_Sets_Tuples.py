#Collection = single "variable" used to store multiple items
#    LIST  = [] ordered and changeable. Duplicated OK.
#    Set   = {} underordered and immutable. but ADD/REMOVE OK. NO Duplicates.
#    Tuple = () ordered and unchangeable. Duplicates OK . FASTER than LIST

fruits = ["apple","banana","orange","strawberry","peach","coconut"]
#printing in reverse order
print(fruits[::-1])

# index = fruits.index("orange")
# print(fruits[index])

for x in fruits:
    print(x)

#length of collection
length = len(fruits)
print(length)

#To check if something is present "in" a list, use in operator (Same as "contains" in java)
print("apple" in fruits)

#Append a new fruit
fruits.append("blueberry")

#insert at a particular index
fruits.insert(4,"Mango")
print(fruits)

print(fruits.count("apple"))


#Indexing of set is not possible. We can only add and remove......