from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

flower_cyan = 38
flower_yellow = 37
count = 0
while True:
	print("count ",count)
	x, y, z = mc.player.getPos()
	if count % 2 == 0:
		print("yellow ")	
		mc.setBlock(x, y, z, flower_yellow)
		sleep(0.1)
	else:
		print("cyan")
		mc.setBlock(x, y, z, flower_cyan)
		sleep(0.1)
	count += 1
	 
