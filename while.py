#ecoding=gbk
unconfirmed_users=['mike','ximon','jick','zuli','perry'];
confirmed_users=[]
while unconfirmed_users:
	confirmed_users.append(unconfirmed_users.pop())
print("All confirmed users are :",end="")
for user in confirmed_users:
	print(user+"  ",end="")

print()

pets=['cat','dog','dog','cat','goldfish','ping','rabbit','cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)

responsers=[]
flag=True
question="Would you like to let another person respond?(yes/no):"
while flag:
	responser={}
	name=input("What is your name?:")
	response=input("Which mountain would you like to climb someday?:")
	responser["name"]=name
	responser["reponse"]=response
	responsers.append(responser)
	if input(question)=='no':
		break
for responser in responsers:
	for k,v in responser.items():
		print(v+"\t",end='')
	print()


























