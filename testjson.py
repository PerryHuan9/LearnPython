#ecoding=gbk

import json

def test():
	numbers=[2,52,3.145,545,3.1551]
	filePath='file/fourth.json'
	with open(filePath,'w')as fourth:
		json.dump(numbers,fourth)

	with open(filePath)as fourth:
		readnumbers=json.load(fourth)
	print(readnumbers)


def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename = 'file/username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		

def login():
	name=get_stored_username()
	if name==None:
		name=input("What's your name?:")
		with open(filePath,'w') as f:
			json.dump(name,f)
			print("Wei'll remember you when you come back,"+name+"!")
	else:
		print('wWecomd back,'+name+"!")




login()





















































