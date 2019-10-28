import bpy
from math import * 
import mathutils
import random 

scn = bpy.context.scene

def RunPerFrame(scene):
    
    #kockice=['d4_1','d6']
    
    ob=bpy.data.objects['d4_1']
    
    #if scn.frame_current == 100:
    #    ob=bpy.data.objects['d6']
    
    ob.rotation_euler = (random.randrange(0,180),random.randrange(0,180),random.randrange(0,180)) 
    ob.location = (random.randrange(-3,3),random.randrange(-2,3),0) 
    
    floor=bpy.data.objects['Pod']
    
    rand=round(random.randrange(1,11))
    
    mat1=bpy.data.materials[str(rand)]
    
    if floor.data.materials:
        floor.data.materials[0]=mat1
    else:
        floor.data.materials.append(mat1)

bpy.app.handlers.frame_change_pre.append(RunPerFrame)
