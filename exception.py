#ecoding=gbk

# try:
	# print(8/0)
# except ZeroDivisionError:
	# print('��������Ϊ0')


def devide():
	print('Give me two number,I will divide them')
	print('Enter "q" to quit')
	while True:
		firstNumber=input('Enter the first number:')
		if firstNumber=='q':
			break
		try:
			secondNumber=input('Enter the second number:')
			answer=int(firstNumber)/int(secondNumber)
			print('the result is:')
		except ZeroDivisionError:
			# print('you can not divide by 0')
			pass #��ʾ���ô���,��������
		else:
			print(answer)

def countWords(filePath):
	"""ͳ�Ƶ�������"""
	try:
		with open(filePath) as f:
			contends=f.read()
	except FileNotFoundError:
		print('sorry,the file '+filePath.split('/').pop()+" does not exit.")
	else:
		# print(contends+'\n')
		words=contends.split()
		print("the file "+filePath.split('/')[-1]+' has '+str(len(words))+" words")



filePaths=['file/third.txt','file/a.txt','file/b.txt','file/c.txt']
for filePath in filePaths:
	countWords(filePath)

devide()






























