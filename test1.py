from mcpi.minecraft import Minecraft

pos = mc.player.getPos()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y+10, z)
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)
dirt = 3
mc.setBlock(x, y, z, dirt)
dirt = block.DIRT.id
mc.setBlock(x, y, z, dirt)
stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)
