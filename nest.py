#ecoding=gbk

#���б���Ƕ���ֵ�
aliens=[]
for number in range(30) :
	alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(alien)
for alien in aliens[:5]:
	print(alien)
	for k,v in alien.items():
		print(k+":"+str(v))
		

pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
	}
for topping in pizza['toppings']:
	print("\t"+topping)
	
	
#���ֵ���Ƕ���б�	
loveLanguage={
		'jen':['python','ruby'],
		'sarah':['c'],
		'edward':['ruby','go'],
		'phil':['python','haskell'],
		}
for name,languages in loveLanguage.items():
	print(name.title()+" love")	
	for language in languages:
		print("\t"+language.title())


#���ֵ���Ƕ���ֵ�	
print()	
books={
		"ʥ��":{"name":"ʥ��",'writer':'����','words':3000000},
		"�۰�":{"name":"�۰�",'writer':'����','words':8000000},
		"��������":{"name":"��������",'writer':'����','words':6000000},
		"ս��":{"name":"ս��",'writer':'����׺�','words':4000000},
		}
for k,v in books.items():
	for key,value in v.items():
		print(key+":"+str(value))
	print()
	

























