from pwn import *

io = process('bingo')

start_script = 'start --set-full-card 1337 --number-of-cards 1337\nb *0x0000555555594544\nc\nb *0x5555555945bc\nc\n'

gdb.attach(io, start_script)
