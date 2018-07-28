from function import showList	


bicycles=['trek','cannondable','redline','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
bicycles.append("ducati")
print(bicycles)
bicycles.insert(0,'motor')
print(bicycles)
del bicycles[2]
print(bicycles)

motor=bicycles.pop()
print(motor)
print(bicycles)
bicycles.pop(0)
print(bicycles)

bicycles.remove("trek")
print(bicycles)

week=["apple",'love',"banana",'orange']
showList(week)
print(week)
week.sort()
print(week)
week.sort(reverse=True)
print(week)
print(sorted(week))
print(sorted(week,reverse=True))

print("the length of week is:"+str(len(week)))
















