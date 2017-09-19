seq = []

while True:
	n = int(input("Digite n: "))    
	if n == 0: break
	seq.append(n)
for i in reversed(seq):
	print(i)
