from pwn import *

conn = remote('0', 9007)
for i in range(0, 31):
  conn.recvline()

for a in range(0, 100):
	output = conn.recvline()
	print(output)
	
	begin = output.find('=')
	end = output.find(' ')
	n = int(output[begin+1:end])
	
	begin = output.find('=', begin+len('='))
	c = int(output[begin+1:])
	
	begin = 0
	end = n/2
	oldend = n
	for j in range(0, c - 1):
	  input = ""
	  for i in range(begin, end):
	    input += str(i) + ' '
	  conn.send(input + '\n')
	  output = conn.recvline()
	  #print("LIMITS: ", begin, end, " OUTPUT: ", output)
	  if int(output) % 10 == 0:
	    begin = end
	    end = (oldend + begin) / 2
	    #My noobness made me write end = oldend earlier...rip
	  else:
	    oldend = end
	    end = (end + begin) / 2
	
	conn.send(str(begin) + '\n') #add in check
	output = conn.recvline()
	print(output)
	if int(output) % 10 != 0:
	  conn.send(str(begin) + '\n')
	else:
	  conn.send(str(end) + '\n')
	
	output = conn.recvline()
	print(output)

output = conn.recvline()
print(output)
conn.interactive()
