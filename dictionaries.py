#coding=gbk
words={
	'mouse':'���',
	'keyboad':'����',
	'laptop':'�ʼǱ�����',
	'calculator':'������',
	'glasses':'�۾�',
	'earphone':'����'}

print(words)
print(words['mouse'])
print(words['laptop'])
words['eyedrop']='��ҩˮ'
words['meal card']='����'
words['unmanned plane']="���˻�"
print(words)
words['unmannedplane']='���˻�'
print(words)

del words['eyedrop']
print(words)

for w,m in words.items():
	print(w+":"+m)

for key in words.keys():
	print(key+":"+words[key])
#sorted()��Ԫ�ؽ�������
for key in sorted(words.keys(),reverse=True):
	print(key)
	
for value in words.values():
	print(value)

#set()��֤�б��е�Ԫ��Ψһ
for value in set(words.values()):
	print(value)


























