import os
list_dirs = os.walk('/usr0/home/senw1/OpenFace/annotation_txt/')
looking_down_intervals = {}
for root, dirs, files in list_dirs:
	for file in files:
		name = file.split('.')[0]
		if len(name):
			looking_down_intervals[name] = []
			with open(root + file) as f:
				for line in f.readlines():
					line = line.strip().split('\t')
					s, e = float(line[3]), float(line[5])
					looking_down_intervals[name].append((s, e))
print looking_down_intervals
