#ecoding=gbk

with open('file/c.txt','w') as f:
	f.write("\t�������\n")
	f.write("\tǧ�����\n")
	f.write('\t����ѩƮ\n')
	f.write('\t����������\n')
	f.write("\tΩ��çç\n")
with open('file/c.txt','r') as f:
	print(f.read())
	
	
with open('file/c.txt','a') as f:
	f.write('\t�������\n')
	f.write('\t��ʧ����\n')
	f.write('\tɽ������\n')
	f.write('\tԭ������\n')
	f.write('\t�����칫�Աȸ�\n')
	f.write('\t������\n')
with open('file/c.txt','r') as f:
	print(f.read())




























