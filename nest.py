#ecoding=gbk

#在列表中嵌套字典
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
	
	
#在字典中嵌套列表	
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


#在字典中嵌套字典	
print()	
books={
		"圣墟":{"name":"圣墟",'writer':'辰东','words':3000000},
		"帝霸":{"name":"帝霸",'writer':'萧生','words':8000000},
		"完美世界":{"name":"完美世界",'writer':'辰东','words':6000000},
		"战天":{"name":"战天",'writer':'苍天白鹤','words':4000000},
		}
for k,v in books.items():
	for key,value in v.items():
		print(key+":"+str(value))
	print()
	

























