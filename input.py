#ecoding=gbk

#测试input()函数
message=input("请输入您的名字：")
print("你好，"+message+"!")
# print(int(message))
# print(float(message))

number=input("Enter a number,and I'll tell you if it is even or odd:")
number=int(number)
if number%2==0:
	print(str(number)+" is even.")
else:
	print(str(number)+" is odd.")
	
#while循环
count=1
while count<=5:
	print("循环"+str(count)+"次")
	count+=1
print()

prompt="Enter something ,I will repeat it back to you"
prompt+="\nEnter quit to end the program:"
message=""
while message!='quit':
	message=input(prompt)
	print(message)  ·



































































