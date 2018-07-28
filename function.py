#ecoding=gbk

def hello(name):
	"""打印 Hello,问候人"""
	print("Hello, "+str(name).title())

def describe_pet(pet_type,name='jinjin'):
	"""描述宠物"""
	print("This is my "+pet_type+",and its name is "+name)
	
def add(a=0,b=0):
	return a+b
	
def buildPersion(firstName,lastName,age=0):
	"""建立persion列表"""
	persion={"first":firstName.title(),"last":lastName.title()}
	if age:
		persion["age"]=age
	return persion

def showList(names):
	"""显示列表"""
	for name in names:
		print("Hello, "+name.title()+".")

def printModels(unprinteds,printeds):
	"""模拟打印模板"""
	while unprinteds:
		model=unprinteds.pop()
		print("printing model")
		printeds.append(model)
		
def makePizza(*toppings):
	"""*号表示可以传入任意数目的参数，并形成一个元组"""
	for topping in toppings:
		print(str(topping)+"\t",end='')
		
def buildPofile(first,last,**info):
	"""**info表示创建一个字典，并将传入的所有键值对参数封装到这个字典中"""
	pofile={"firstName":first.title(),'lastName':last.title()}
	for k,v in info.items():
		pofile[k]=v
	return pofile


# describe_pet("狗",'包子')
# describe_pet(pet_type='cat',name='kaka')
# hello('黄益凛')
# describe_pet('rabbit')
# print(add(3.14,8))
# print(buildPersion("perry","huang",18))
# names=['perry','ximon','zudi','jack']
# showList(names)

# unprintedModels=['iphone case','robot pendant','dodecahedron']
# printedModels=['Huawei case']
# printModels(unprintedModels[:],printedModels)
# print(printedModels)
# print(unprintedModels)

# makePizza('香橙')
# makePizza('苹果','石榴','香蕉',88520)
# print()
# pofile=buildPofile('perry',"huang",age=21,sex="男",身份="学生")
# print(pofile)
































