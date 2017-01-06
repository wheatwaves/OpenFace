import os
annotation_dirs = os.walk('/Users/wheatwaves/Desktop/suicidality analysis/OpenFace/new_annotation_txt/')
looking_down_intervals = {}
discarded_intervals = {}
for root, dirs, files in annotation_dirs:
	for file in files:
		name = file.split('.')[0]
		if len(name):
			looking_down_intervals[name] = []
			discarded_intervals[name] = []
			with open(root + file) as f:
				for line in f.readlines():
					line = line.strip().split('\t')
					s, e = float(line[3]), float(line[5])
					# process data on edges
					if e - s > 0.5:
						s += 0.2
						e -= 0.2
						discarded_intervals[name].append((s,s+0.2))
						discarded_intervals[name].append((e-0.2,e))
					else:
						interval_time = e - s
						s += 0.3 * interval_time
						e -= 0.3 * interval_time
						discarded_intervals[name].append((s,s+0.2*interval_time))
						discarded_intervals[name].append((e-0.2*interval_time,e))
					looking_down_intervals[name].append((s, e))
feature_dirs = os.walk('/Users/wheatwaves/Desktop/suicidality analysis/OpenFace/normalized_output_features/')
for root, dirs, files in feature_dirs:
	for file in files:
		name = file.strip()
		if len(name):
			if name in looking_down_intervals.keys():
				with open(root + file) as f:
					for line in f.readlines():
						timestamp = float(line.split(',')[0].strip())
						discarded = False
						for interval in discarded_intervals[name]:
							if timestamp >= interval[0] and timestamp <= interval[1]:
								discarded = True
								break
						if discarded:
							continue
						flag = False
						for interval in looking_down_intervals[name]:
							if timestamp >= interval[0] and timestamp <= interval[1]:
								flag = True
								break
						if flag:
							with open('/Users/wheatwaves/Desktop/suicidality analysis/OpenFace/new_normalized_training_data/' + name + '_positive.txt', 'a') as g:
								g.write(line)
						else :
							with open('/Users/wheatwaves/Desktop/suicidality analysis/OpenFace/new_normalized_training_data/' + name + '_negative.txt', 'a') as g:
								g.write(line)


