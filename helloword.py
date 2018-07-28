message="Hello Python world!!!!!"
print(message)

message='"I love you "I say'
print(message)

name="COMMUNICATION PROJect"
print(name.title())
print(name.upper())
print(name.lower())

firstName="perry"
lastName="Huang"
fullName=firstName+" "+lastName
print(fullName.title())
print(("perry"+" huang").title())

age=21
birthday="happy "+str(age)+"rd birthday"
print(birthday.title())

from function import describe_pet as dp
dp('dog')

print("***************************************************************")
filePath='F:\PythonProject\file\second.txt'
with open(filePath) as second:
	contents=second.read()
	print(contents)

