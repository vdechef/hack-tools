import os.path
import time
from pwn import *

TTYPATH = '/dev/ttyUSB0'
BAUDRATE = 57600
SHELL_INTERACT = "MT7628 #"
OUTFILE = "./firmware.txt"
BLOCK_SIZE = 1024
BLOCK_PER_PAGE = 64   # 64kB per memory page
NUM_PAGES = 256

print("wait for device")
while(not os.path.exists(TTYPATH)):
    time.sleep(1)

print("init serial")

io = serialtube(TTYPATH, baudrate=BAUDRATE)

print("device connected")

io.recvuntil("Please choose the operation")

print(f"Force choose U-Boot")

io.send("4")

io.recvuntil(SHELL_INTERACT)
io.close() # need to close otherwise buffer is corrupted between reads

print("Ready to dump")

with open(OUTFILE, "wb") as f:
    # loop over each memory block, connecting and disconnecting the serial for each block to avoid memory corruption in pwntool
    numBlocks = BLOCK_PER_PAGE * NUM_PAGES
    for i in range(0, numBlocks -1):
        io = serialtube(TTYPATH, baudrate=BAUDRATE)
        io.clean() # need to clean otherwise buffer's first bytes are corrupted

        addrStart = hex(i*BLOCK_SIZE)
        readSize = hex(BLOCK_SIZE)
        cmd = f"spi read {addrStart[2:]} {readSize[2:]}" # [2:] is to remove 0x prefix]
        print(f"Dumping: {cmd}")
        
        io.sendline(cmd)
        res = io.recvuntil(SHELL_INTERACT)

        # keep only data from resulting output (ie. remove commandline logging)
        data = res[len(cmd)+19:-10]
        
        # append into resulting file
        #print(data)
        f.write(data)
        
        io.close() # need to close otherwise buffer is corrupted between reads
        time.sleep(0.5)

print("done")
