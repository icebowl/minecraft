from time import sleep
from mcpi.minecraft import Minecraft	
from mcpi import block
def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	#ase(mc, x, y, z+5)
	tower(mc, x+5, y, z+10)	
	#counter_weight(mc, x+20, y, z+20)
	#def counter_weight (mc, x, y, z, xadd,yadd, zadd, height):	
	counter_weight(mc, x+5, y, z+10, 10,10,10, 50)	
	
def init():      
	mc = Minecraft.create()   
	x, y, z = mc.player.getPos()   
	return mc
 
def base (mc, x, y, z):
	iron_block = 42
	mc.setBlocks(x, y, z, x+10, y, z+10, iron_block) 
	mc.setBlocks(x+1, y+1, z+1, x+9, y+1, z+9, iron_block)
	mc.setBlocks(x+2, y+2, z+2, x+8, y+2, z+8, iron_block)
	mc.setBlocks(x+3, y+3, z+3, x+7, y+3, z+7, iron_block)
	mc.setBlocks(x+4, y+4, z+4, x+6, y+4, z+6, iron_block)
	mc.setBlocks(x+5, y+5, z+5, x+5, y+5, z+5, iron_block)
	
def counter_weight (mc, x, y, z, xadd,yadd, zadd, height):
	lapis = 22 	  
	x = x - (xadd / 2)
	z = z - (zadd / 2)
	mc.setBlocks(x, y+height, z, x+xadd, y+yadd+height, z+zadd, lapis)

def tower (mc, x, y, z):
	diamond = 57
	for k in range(0,1024):
			mc.setBlock(x, y+k, z,diamond)
#main    
main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
