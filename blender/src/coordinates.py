import bpy
import bpy_extras
import json


def my_handler(scene):
    obj = bpy.data.objects['Camera']
    co = bpy.data.objects["d4_1"].location

    co_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, co)
    print("2D Coords:", co_2d)

    # pixel coords
    render_scale = scene.render.resolution_percentage / 100
    render_size = (
        int(scene.render.resolution_x * render_scale),
        int(scene.render.resolution_y * render_scale),
        )
              
    coords = {
        "dice": bpy.data.objects["d4_1"].name,
        "x": round(co_2d.x * render_size[0]),
        "y": round(co_2d.y * render_size[1])
        }
        
    with open("coords.json", "a") as file:
        json.dump(coords, file, indent=4)

try:
    bpy.app.handlers.render_post.remove(my_handler)
except ValueError:
    pass

bpy.app.handlers.render_post.append(my_handler)

