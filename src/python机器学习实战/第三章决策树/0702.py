# AUTHOR lijixin

filename='trees.py'
with open(filename,'r',encoding='utf-8')as fp:
	lines=fp.readlines()
	print(lines)
	maxLength=max(map(len,lines))
for index,line in enumerate(lines):
	newLine=line.lstrip()
	# newLine=newLine+' '*(maxLength+5-len(newLine))
	newLine=newLine+'#'+str(index+1)+'\n'
	lines[index]=newLine
with open(filename[:-3]+'_new.py','w')as fp:
		fp.writelines(lines)
