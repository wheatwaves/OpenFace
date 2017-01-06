import os
data_dir = os.walk(/usr1/projects/cchmc/dataset/shared_cchmc/)
f = open('all_file_name','w')
for root, dirs, files in data_dir:
	for file in files:
		f.write(file)
		f.write('\n')
f.close()
