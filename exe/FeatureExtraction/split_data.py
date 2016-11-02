import os
annotation_dirs = os.walk('/usr0/home/senw1/OpenFace/annotation_txt/')
looking_down_intervals = {}
for root, dirs, files in annotation_dirs:
	for file in files:
		name = file.split('.')[0]
		if len(name):
			looking_down_intervals[name] = []
			with open(root + file) as f:
				for line in f.readlines():
					line = line.strip().split('\t')
					s, e = float(line[3]), float(line[5])
					looking_down_intervals[name].append((s, e))
feature_dirs = os.walk('/usr0/home/senw1/OpenFace/output_features/')
for root, dirs, files in feature_dirs:
	for file in files:
		name = file.split('.')[0]
		if len(name):
			if name in looking_down_intervals.keys():
				with open(root + file) as f:
					for line in f.readlines()[1:]:
						timestamp = float(line.split(',')[1].strip())
						flag = False
						for interval in looking_down_intervals[name]:
							if timestamp >= interval[0] and timestamp <= interval[1]:
								flag = True
								break
						if flag:
							with open('/usr0/home/senw1/OpenFace/training_data/positive.txt', 'a') as g:
								g.write(line)
						else:
							with open('/usr0/home/senw1/OpenFace/training_data/negative.txt', 'a') as g:
								g.write(line)


