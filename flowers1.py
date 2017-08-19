from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

flower_cyan = 38
flower_yellow = 37
count = 0
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower_cyan)
    sleep(0.1)
    count += 1
    if count % 2 == 0:
		mc.setBlock(x, y, z, flower_yellow)
	if (count > 1000): 
		break
	
