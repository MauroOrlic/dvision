import bpy
from math import * 
import mathutils
import random 
import bpy_extras

#0,0,0->4->1  0,251,0->2->4  248,28,0->1->2 112,388,0->3->3
#45,37,0->5  225,37,0->2  135,37,0->8  315,37,0->3 227,-35.9,0->4  133,-35.9,0->6  47,-35.9,0->7  313,-35.9,0->1
#50,0,0->2  20,133,0->5  136,153,0->0  136,207,0->4  20,227,0->3  -43,208,0->1  50,180,0->9  201,227,0->6  142,391,0->7  20,47,0->8
#117,0,0->12  297,0,0->5  414,0,0->11  594,0,0->6  117,120,0->1  297,120,0->3  0,31.7,0->4  180,31.7,0->2  90,238,0->9  90,302,0->7  180,212,0->10  180,-32,0->8
#159,0,0->19  201,0,0->9  -20.9,0,0->2  20.9,0,0->12  44.9,35.2,0->10  135,35.2,0->3  225,35.2,0->6  316,34.3,0->20  90,20.5,0->17  90,159,0->14  90,201,0->4  90,-381,0->7  180,-471,0->5  180,-609,0->8  180,-651,0->16  180,429,0->13  -45,-505,0->1  225,-35.1,0->11  45.1,-35.1,0->15  135,215,0->18

scn = bpy.context.scene
brojic = 1
rezolucija = 416

def RunPerFrame(scene):
    global brojic
    global rezolucija
    
    kockiceSve=['d4_1','d4_2','d6','d8','d10','d12','d20','d100_1','d100_2',
    'd4_1.001','d4_2.001','d6.001','d8.001','d10.001','d12.001','d20.001','d100_1.001','d100_2.001',
    'd4_1.002','d4_2.002','d6.002','d8.002','d10.002','d12.002','d20.002','d100_1.002','d100_2.002',
    'd4_1.003','d4_2.003','d6.003','d8.003','d10.003','d12.003','d20.003','d100_1.003','d100_2.003',
    'd4_1.004','d4_2.004','d6.004','d8.004','d10.004','d12.004','d20.004','d100_1.004','d100_2.004',
    'd4_1.005','d4_2.005','d6.005','d8.005','d10.005','d12.005','d20.005','d100_1.005','d100_2.005',
    'd4_1.006','d4_2.006','d6.006','d8.006','d10.006','d12.006','d20.006','d100_1.006','d100_2.006',
    'd4_1.007','d4_2.007','d6.007','d8.007','d10.007','d12.007','d20.007','d100_1.007','d100_2.007',
    'd4_1.008','d4_2.008','d6.008','d8.008','d10.008','d12.008','d20.008','d100_1.008','d100_2.008']

    kockice_names = ["d4_1","d4_2","d4_3","d4_4","d6_1","d6_2","d6_3","d6_4","d6_5","d6_6","d8_1","d8_2",
                    "d8_3","d8_4","d8_5","d8_6","d8_7","d8_8","d10_1","d10_2","d10_3","d10_4","d10_5","d10_6",
                    "d10_7","d10_8","d10_9","d10_10","d12_1","d12_2","d12_3","d12_4","d12_5","d12_6","d12_7",
                    "d12_8","d12_9","d12_10","d12_11","d12_12","d20_1","d20_2","d20_3","d20_4","d20_5","d20_6",
                    "d20_7","d20_8","d20_9","d20_10","d20_11","d20_12","d20_13","d20_14","d20_15","d20_16",
                    "d20_17","d20_18","d20_19","d20_20","d100_00","d100_10","d100_20","d100_30","d100_40",
                    "d100_50","d100_60","d100_70","d100_80","d100_90"]
    
    for i in range(len(kockiceSve)):
            ob = bpy.data.objects[kockiceSve[i]]
            ob.location = (30,0,0)

    kockice = []
    kockice = random.sample(kockiceSve, random.randrange(2,8))

    potentional_coords = []
    x_duljina = 9
    y_duljina = 9
    for i in range(0, 4):
        for j in range (0,4):
            sredina_x = ( i * 2 + 1 ) * x_duljina / 9 # broj_tocaka * 2 + 1  je ovo 9
            sredina_y = ( j * 2 + 1) * y_duljina / 9
            sredina_x = sredina_x - 4
            sredina_y = sredina_y - 4
            potentional_coords.append( (sredina_x, sredina_y, 0))

    the_coords = random.sample(potentional_coords, len(kockice))

    for i in range(len(kockice)):
        ob = bpy.data.objects[kockice[i]]
        ob.location = the_coords[i]
        
        rotateD6 = [(radians(180),0,radians(random.randrange(0,360))), 
                    (radians(270),0,radians(random.randrange(0,360))), 
                    (0,radians(270),radians(random.randrange(0,360))), 
                    (0,radians(90),radians(random.randrange(0,360))), 
                    (radians(90),0,radians(random.randrange(0,360))),
                    (0,0,radians(random.randrange(0,360)))] 

        rotateD4 = [(radians(248),radians(28),radians(random.randrange(0,360))),
                    (0,radians(251),radians(random.randrange(0,360))),
                    (radians(112),radians(388),radians(random.randrange(0,360))),
                    (0,0,radians(random.randrange(0,360)))]

        rotateD8 = [(radians(313),radians(-35.9),radians(random.randrange(0,360))),
                    (radians(225),radians(37),radians(random.randrange(0,360))),
                    (radians(315),radians(37),radians(random.randrange(0,360))),
                    (radians(227),radians(-35.9),radians(random.randrange(0,360))),
                	(radians(45),radians(37),radians(random.randrange(0,360))),
                    (radians(133),radians(-35.9),radians(random.randrange(0,360))),
                    (radians(47),radians(-35.9),radians(random.randrange(0,360))),
                    (radians(135),radians(37),radians(random.randrange(0,360)))] 

        rotateD10 = [(radians(-43),radians(208),radians(random.randrange(0,360))),
                    (radians(50),0,radians(random.randrange(0,360))),
                    (radians(20),radians(227),radians(random.randrange(0,360))),
                    (radians(136),radians(207),radians(random.randrange(0,360))),
                    (radians(20),radians(133),radians(random.randrange(0,360))),
                    (radians(201),radians(227),radians(random.randrange(0,360))),
                    (radians(142),radians(391),radians(random.randrange(0,360))),
                    (radians(20),radians(47),radians(random.randrange(0,360))),
                    (radians(50),radians(180),radians(random.randrange(0,360))),
                    (radians(136),radians(153),radians(random.randrange(0,360)))]

        rotateD12 = [(radians(117),radians(120),radians(random.randrange(0,360))),
                    (radians(180),radians(31.7),radians(random.randrange(0,360))),
                    (radians(297),radians(120),radians(random.randrange(0,360))),
                    (0,radians(31.7),radians(random.randrange(0,360))),
                    (radians(297),0,radians(random.randrange(0,360))),
                    (radians(594),0,radians(random.randrange(0,360))),
                    (radians(90),radians(302),radians(random.randrange(0,360))),
                    (radians(180),radians(-32),radians(random.randrange(0,360))),
                    (radians(90),radians(238),radians(random.randrange(0,360))),
                    (radians(180),radians(212),radians(random.randrange(0,360))),
                    (radians(414),0,radians(random.randrange(0,360))),
                    (radians(117),0,radians(random.randrange(0,360)))]

        rotateD20 = [(radians(-45),radians(-505),radians(random.randrange(0,360))),
                    (radians(-20.9),0,radians(random.randrange(0,360))),
                    (radians(135),radians(35.2),radians(random.randrange(0,360))),
                    (radians(90),radians(201),radians(random.randrange(0,360))),
                    (radians(180),radians(-471),radians(random.randrange(0,360))),
                    (radians(225),radians(35.2),radians(random.randrange(0,360))),
                    (radians(90),radians(-381),radians(random.randrange(0,360))),
                    (radians(180),radians(-609),radians(random.randrange(0,360))),
                    (radians(201),0,radians(random.randrange(0,360))),
                    (radians(44.9),radians(35.2),radians(random.randrange(0,360))),
                    (radians(225),radians(-35.1),radians(random.randrange(0,360))),
                    (radians(20.9),0,radians(random.randrange(0,360))),
                    (radians(180),radians(291),radians(random.randrange(0,360))),
                    (radians(90),radians(159),radians(random.randrange(0,360))),
                    (radians(45.1),radians(-35.1),radians(random.randrange(0,360))),
                    (radians(180),radians(-291),radians(random.randrange(0,360))),
                    (radians(90),radians(20.5),radians(random.randrange(0,360))),
                    (radians(135),radians(215),radians(random.randrange(0,360))),
                    (radians(159),0,radians(random.randrange(0,360))),
                    (radians(316),radians(34.3),radians(random.randrange(0,360)))]

        randomRotacijaD6 = random.randrange(0,6)
        randomRotacijaD4 = random.randrange(0,4)
        randomRotacijaD8 = random.randrange(0,8)
        randomRotacijaD10 = random.randrange(0,10)
        randomRotacijaD100_1 = random.randrange(0,10)
        randomRotacijaD100_2 = random.randrange(0,10)
        randomRotacijaD12 = random.randrange(0,12)
        randomRotacijaD20 = random.randrange(0,20)
        rotation_d4_alt = [2,4,3,1]
        rotation_d100_alt = [2,3,4,5,6,7,8,9,10,1]
        
        file1 = open("/home/sanja/Desktop/Koordinate/"+str(brojic).zfill(7)+".txt","a") 

        if kockice[i].startswith('d6'):
            #velicina kockice -> 50,60 w,h
            ob.rotation_euler = rotateD6[randomRotacijaD6]
            brojD6 = randomRotacijaD6 + 1
            name = 'd6_' + str(brojD6)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)

            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*33*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*33*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d4_2'):
            #velicina kockice -> 57,52 w,h
            ob.rotation_euler = rotateD4[randomRotacijaD4]
            brojD4_1 = randomRotacijaD4 + 1
            name = 'd4_' + str(brojD4_1)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = ((round(co_2d.x * render_size[0])+(2*32*1.04)))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*32*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d4_1'):
            ob.rotation_euler = rotateD4[randomRotacijaD4]
            brojD4_2 = rotation_d4_alt[randomRotacijaD4]
            name = 'd4_' + str(brojD4_2)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*32*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*32*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d8'):
            #velicina kockice -> 52.5,48.5 w,h
            ob.rotation_euler = rotateD8[randomRotacijaD8]
            brojD8 = randomRotacijaD8 + 1
            name = 'd8_' + str(brojD8)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*31*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*31*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d10.') or kockice[i] == ('d10'):
            #velicina kockice -> 54,58.5 w,h
            ob.rotation_euler = rotateD10[randomRotacijaD10]
            brojD10 = randomRotacijaD10 + 1
            name = 'd10_' + str(brojD10)
            id_kocke = kockice_names.index(name)
            #aaaaaaaaaa
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*32*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*32*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy
            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d100_1'):
            ob.rotation_euler = rotateD10[randomRotacijaD10]
            brojD100_1 = rotation_d100_alt[randomRotacijaD10]
            if (brojD100_1 == 1): 
                name = 'd100_00'
            else:
                name = 'd100_' + str((brojD100_1 - 1) * 10)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*32*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*32*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d100_2'):
            ob.rotation_euler = rotateD10[randomRotacijaD10]
            brojD100_2 = rotation_d100_alt[randomRotacijaD10]
            if (brojD100_2 == 1): 
                name = 'd100_00'
            else:
                name = 'd100_' + str((brojD100_2 - 1) * 10)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*32*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*32*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d12'):
            #velicina kockice -> 71.5,72 w,h
            ob.rotation_euler = rotateD12[randomRotacijaD12]
            brojD12 = randomRotacijaD12 + 1
            name = 'd12_' + str(brojD12)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*38*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*38*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
        if kockice[i].startswith('d20'):
            #velicina kockice -> 73,67 w,h
            ob.rotation_euler = rotateD20[randomRotacijaD20]
            brojD20 = randomRotacijaD20 + 1
            name = 'd20_' + str(brojD20)
            id_kocke = kockice_names.index(name)
            #print(name, id_kocke)
            obj = bpy.data.objects['Camera']
            co = ob.location
            co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
            render_scale = scene.render.resolution_percentage / 100
            render_size = (
                int(scene.render.resolution_x * render_scale),
                int(scene.render.resolution_y * render_scale),
                )
            gornjaLijevox = (round(co_2d.x * render_size[0]))/rezolucija
            gornjaLijevoy = 1 - ((round(co_2d.y * render_size[1]))/rezolucija)

            donjaDesnox = (round(co_2d.x * render_size[0])+(2*38*1.04))/rezolucija
            donjaDesnoy = 1 - ((round(co_2d.y * render_size[1])-(2*38*1.04))/rezolucija)

            donjaDesnox = donjaDesnox - gornjaLijevox
            donjaDesnoy = donjaDesnoy - gornjaLijevoy

            file1.writelines(str(id_kocke)+' '+str(gornjaLijevox)+' '+str(gornjaLijevoy)+' '+str(donjaDesnox)+' '+str(donjaDesnoy)+'\n') 
      

    brojic = brojic +1
    #ob=bpy.data.objects['d4_1']
    floor=bpy.data.objects['Pod']
    
    rand=round(random.randrange(1,11))
    
    mat1=bpy.data.materials[str(rand)]
    
    if floor.data.materials:
        floor.data.materials[0]=mat1
    else:
        floor.data.materials.append(mat1)

bpy.app.handlers.frame_change_pre.append(RunPerFrame)
