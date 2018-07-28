fruit=['apple','range','banana','pear']
for f in fruit:
	print(f)
	print(f+' is good\n')
print('that is all,thanks\n')

for value in range(1,5):
	print(value)
	
numbers=list(range(1,10))
print(numbers)

even_numbers=list(range(2,12,2))
print(even_numbers)

squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares=[value**3 for value in range(1,11)]
print(squares)


	
































