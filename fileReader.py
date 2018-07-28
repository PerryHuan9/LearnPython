#ecoding=gbk

def read_file():
	with open('pi.txt') as file_object:
		contents=file_object.read()
		print(contents.rstrip())

	with open( 'file/a.txt') as firsts:
		contents=firsts.read()
		print(contents)
		
	filePath='F:/PythonProject/file/second.txt'
	with open(filePath) as second:
		contents=second.read()
		print(contents)

	with open(filePath) as f:
		for line in f:
			print(line.rstrip())
			
	with open(filePath) as f:
		lines=f.readlines()
	for line in lines[:2]:
		print(line.rstrip())

def translate():
	fileStr=''
	with open('file/c.txt') as f:
		lines=f.readlines()
	for line in lines:
		fileStr+=line.strip()
	print(fileStr)
	print(float(fileStr)+1)



	

def isBirthdayInPI(birthday):
	with open('pi.txt') as pi:
		lines=pi.readlines()
	fileStr=''
	for line in lines:
		fileStr+=line.strip().replace(' ','')
	if birthday in fileStr:
		print('your birthday is in PI')
	else:
		print('your birthday is not in PI')

# birthday=input('Enter your birthday:')
# isBirthdayInPI(birthday)


		













