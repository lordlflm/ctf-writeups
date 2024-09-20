from pwn import *

flag2 = 'flag-such_crypto_much_wow'

io = process(['reverseme', '--debug-enable'])
io.recv() 
io.sendline(flag2.encode())
io.recv()

res = 'nndrdylrsmvzswybaxlul'
p2 = ['4','3','9','7','3','2','9', '3', '3', '2', '2','5','9','9','5','3', '4','3','2','7', '7']
p3 = [0xa3,0xa2,0xa2,0x97,0xa2,0x9e,0xa0,0x9a,0x9f,0x9d,0x9c,0xa2,0x9f,0xa0,0x9f,0xa0,0x9b,0x92,0x99,0x9b,0x9f]
flag3 = ''
len = 21
alpha = list(string.ascii_letters)

for i in range(21):
    for c in alpha:
        if ((ord(c) - 0x61 + p3[i] * ord(p2[i])) % 0x100 + 0x61 + ord(p2[i]) * 0x100) % 0x1a + 0x61 == ord(res[i]):
            flag3 += c
            break

# fix because we are getting 'symbolicexecutionesop' while 'symbolicexecutionisop' is the right password
flag3 = flag3[:17] + 'i' + flag3[18:]
print(flag3)
io.sendline(flag3.encode())
io.interactive()
