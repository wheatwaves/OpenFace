import os
with open('filename.txt') as f:
	for line in f.readlines():
		filename = line.strip()
		os.system('/usr0/home/senw1/OpenFace/build/bin/FeatureExtraction -rigid -verbose -f "/usr1/projects/cchmc/dataset/shared_cchmc/' + filename
			+ '" -of "/usr0/home/senw1/OpenFace/output_features/' + filename + '.txt" -q')