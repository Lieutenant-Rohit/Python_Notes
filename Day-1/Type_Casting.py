#TypeCasting - The process of converting a value of one data type to another.
#              There are two types of typecasting.
#              1-->Explicit || 2 -->Implicit

name = "Bro"
age = 24
CGPA = 9.2
student = True

#type() is used to get the typeof a variable.
print(type(name))
print(type(age))
print(type(CGPA))

#Explicit Conversion
#int ---> float
age = float(age)
print("Age type:", type(age))
print(f"Age is {age}. ")

#boolean ---> string
student = str(student)
print(f"Student is {student}.")
print(f"Student type is {type(student)}.")

#float ----> Boolean
age = bool(age)
print(f"Age is {age}.")

#IMPLICIT TYPE CASTING - Conversion is automatically.
x=2
y=2.0
x=x/y
print(x)

