#ecoding=gbk

with open('file/c.txt','w') as f:
	f.write("\t北国风光\n")
	f.write("\t千里冰封\n")
	f.write('\t万里雪飘\n')
	f.write('\t望长城内外\n')
	f.write("\t惟余莽莽\n")
with open('file/c.txt','r') as f:
	print(f.read())
	
	
with open('file/c.txt','a') as f:
	f.write('\t大河上下\n')
	f.write('\t顿失滔滔\n')
	f.write('\t山舞银蛇\n')
	f.write('\t原驰蜡象\n')
	f.write('\t欲与天公试比高\n')
	f.write('\t须晴日\n')
with open('file/c.txt','r') as f:
	print(f.read())




























