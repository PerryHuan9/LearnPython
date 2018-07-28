#coding=gbk
words={
	'mouse':'鼠标',
	'keyboad':'键盘',
	'laptop':'笔记本电脑',
	'calculator':'计算器',
	'glasses':'眼镜',
	'earphone':'耳机'}

print(words)
print(words['mouse'])
print(words['laptop'])
words['eyedrop']='眼药水'
words['meal card']='饭卡'
words['unmanned plane']="无人机"
print(words)
words['unmannedplane']='无人机'
print(words)

del words['eyedrop']
print(words)

for w,m in words.items():
	print(w+":"+m)

for key in words.keys():
	print(key+":"+words[key])
#sorted()对元素进行排序
for key in sorted(words.keys(),reverse=True):
	print(key)
	
for value in words.values():
	print(value)

#set()保证列表中的元素唯一
for value in set(words.values()):
	print(value)


























