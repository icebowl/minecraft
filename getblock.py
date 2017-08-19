#getblock.py
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)
    print(block_beneath)spNew thread
