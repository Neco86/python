datals = []
f =open("AutoTranceDraw_data.txt")
for line in f:
	line = line.replace("\n","")
	datals.append(list(map(eval,line.split(","))))
	#print('line.split(",")',line.split(","))									#['300', '0', '144', '1', '0', '0']
	#print('map(eval,line.split(","))',map(eval,line.split(",")))
	#print('list(map(eval,line.split(",")))',list(map(eval,line.split(","))))	#[300, 0, 144, 1, 0, 0]
f.close()
'''
print(datals)
[[300, 0, 144, 1, 0, 0], [300, 0, 144, 0, 1, 0], [300, 0, 144, 0, 0, 1], [300, 0, 144, 1, 1, 0], [300, 0, 144, 0, 1, 1], [184, 0, 72, 1, 0, 1], [184, 0, 72, 0, 0, 0], [184, 0, 72, 0, 0, 0], [184, 0, 72, 0, 0, 0], [184, 1, 72, 1, 0, 1], [184, 1, 72, 0, 0, 0], [184, 1, 72, 0, 0, 0], [184, 1, 72, 0, 0, 0], [184, 1, 72, 0, 0, 0], [184, 1, 720, 0, 0, 0]]
'''