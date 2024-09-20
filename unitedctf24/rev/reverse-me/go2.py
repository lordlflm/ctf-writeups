from pwn import *

io = process(['reverseme', '--debug-enable'])

enc = '2f14575e55304b5e171c572a15240d2c721c165a291e2e321677'
# every 2 characters of enc is 
enc_hex = [0x2f, 0x14, 0x57, 0x5e, 0x55, 0x30, 0x4b, 0x5e, 0x17, 0x1c, 0x57, 0x2a, 0x15, 0x24, 0x0d, 0x2c, 0x72, 0x1c, 0x16, 0x5a, 0x29, 0x1e, 0x2e, 0x32, 0x16, 0x77]
v = 'Na10cZ14xJ3QwmrJ4xz0JHPDxp7'
len = 26

flag = ''
for i in range(len):
    enc_hex[i] -= 7
    res = (ord(v[i]) ^ enc_hex[i])
    flag += chr(res)

io.recv() 
io.sendline(flag.encode())
io.interactive()
