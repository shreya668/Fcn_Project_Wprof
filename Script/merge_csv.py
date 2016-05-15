import sys

i = 1
res_dict = {}
keys = set()
print len(sys.argv)

while i < len(sys.argv):
	fname = sys.argv[i]
	fo =  open(fname, 'r')
	temp = {}

        common_keys = set()
	for line in fo.readlines():
		split_line = line.split(',')
		if i== 1:
			keys.add(split_line[0])
		if i > 1 :
			if split_line[0] in keys:
				common_keys.add(split_line[0])	
				
		temp[split_line[0]] = str(line).replace("\n","")
	#print keys
	#print common_keys
	if i > 1:
		keys = common_keys

	res_dict[fname] = temp
	i = i+1
	fo.close()

final_dict = {}
#output = open('merge_desktop.csv', 'w')
output = open('new_desktop.csv', 'w')
i = 0
print len(keys)
print keys

for fname in res_dict:
	print fname
	for site in res_dict[fname]:
		if site in keys:
			#print str(res_dict[fname][site])
			output.write(str(res_dict[fname][site])+","+str(i)+'\n')
	
	i = i+1


output.close()	
