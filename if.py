# coding=gbk
cars=['audi','bwm','subaru','toyota']
for car in cars:
	if car=='bwm':
		print(car.upper())
	else:
		print(car.title())
print('audi' not in cars)
print('audi' in cars)

age=12
if age<4:
	print('Your admisson cost is $0.')
elif age<18:
	print('Your admission cost is $5.')
else:
	print('Your admisson cost is $10.')
	

requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
	print('Add pepperoni')
elif 'extra cheese'in requested_toppings:
	print("Add extra cheese")

available_toppings=['mushrooms','olives','green peppers',
					'pepperoni','pineapple','extra cheese']	
for topping in requested_toppings:
	if topping in available_toppings:
		print('Adding'+ topping)
	else:
		print("sorry,we don't  have "+topping)
print("我爱你")
					
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
