import pickle
import os
import csv
import collections
import sys

#path = "./desktop_wifi_without_cache/temp_files/wprof_300_5_pro_1"
path = str(sys.argv[1])
dirs = os.listdir(path)
res = ""
#csvfile = open("desk_without_new.csv","w")
csvfile = open(str(sys.argv[2]), "w")
#required = ["time_download"]
required = ["time_download", "download_dns","time_download_html","time_download_css","time_download_js","time_download_img","time_download_o","time_comp"]
writer = csv.writer(csvfile, delimiter=',')
dict_res = {}
for files in dirs:
	name = files
	name = name.replace("original.testbed.localhost_www.","")
	files = os.path.join(path,files)
	file_1 = open(files,"rb")
	lines = file_1.readlines()
	for row in lines:
		list_res = row.rstrip("\n").split("\t")
		list_res[0] = list_res[0].replace(":","")
		if list_res[0] in required:# and float(list_res[1]) > 0.0:
			#print list_res[1]
			writer.writerow([name,list_res[0],list_res[1]])
			#print row 
			#dict_res[name] = (list_res[0], list_res[1])
	        #for key,value in dict.items():
			#if key in required:
			#spamwriter.writerow([name,key,str(value)])


#od = collections.OrderedDict(sorted(dict_res.items()))
#for key in od:
#	writer.writerow([key, od[key][0], od[key][1]])

