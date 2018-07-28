players=['charles','martina','michael','florence','eli','eli']
print(players)
print(players[1:3])
print(players[:4])
print(players[2:])
for player in players[:3]:
	print(player)

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print(friend_foods)

my_foods.insert(0,'cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

finalValue=('PI',3.14159,'C',3*10**6)
print(finalValue)
for value in finalValue:
	print(value)
finalValue=('PI',3.14159)
print(finalValue)


	 
