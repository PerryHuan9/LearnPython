#ecoding=gbk

def hello(name):
	"""��ӡ Hello,�ʺ���"""
	print("Hello, "+str(name).title())

def describe_pet(pet_type,name='jinjin'):
	"""��������"""
	print("This is my "+pet_type+",and its name is "+name)
	
def add(a=0,b=0):
	return a+b
	
def buildPersion(firstName,lastName,age=0):
	"""����persion�б�"""
	persion={"first":firstName.title(),"last":lastName.title()}
	if age:
		persion["age"]=age
	return persion

def showList(names):
	"""��ʾ�б�"""
	for name in names:
		print("Hello, "+name.title()+".")

def printModels(unprinteds,printeds):
	"""ģ���ӡģ��"""
	while unprinteds:
		model=unprinteds.pop()
		print("printing model")
		printeds.append(model)
		
def makePizza(*toppings):
	"""*�ű�ʾ���Դ���������Ŀ�Ĳ��������γ�һ��Ԫ��"""
	for topping in toppings:
		print(str(topping)+"\t",end='')
		
def buildPofile(first,last,**info):
	"""**info��ʾ����һ���ֵ䣬������������м�ֵ�Բ�����װ������ֵ���"""
	pofile={"firstName":first.title(),'lastName':last.title()}
	for k,v in info.items():
		pofile[k]=v
	return pofile


# describe_pet("��",'����')
# describe_pet(pet_type='cat',name='kaka')
# hello('������')
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

# makePizza('���')
# makePizza('ƻ��','ʯ��','�㽶',88520)
# print()
# pofile=buildPofile('perry',"huang",age=21,sex="��",���="ѧ��")
# print(pofile)
































