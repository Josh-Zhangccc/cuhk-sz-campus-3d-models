import bpy
import sys
from mathutils import Vector

scene_name = sys.argv[-1]
root = r"D:/My Programs/Unity Programs/cuhk_sz_models_backup"
blend_path = root + "/gltf_export/" + scene_name + "/" + scene_name + ".blend"
png_path = root + "/gltf_export/" + scene_name + "/" + scene_name + "_preview.png"

bpy.ops.wm.open_mainfile(filepath=blend_path)

# world-space bounding box of all mesh objects
meshes = [o for o in bpy.data.objects if o.type == "MESH"]
mn = Vector((1e12, 1e12, 1e12))
mx = Vector((-1e12, -1e12, -1e12))
for o in meshes:
    for c in o.bound_box:
        w = o.matrix_world @ Vector(c)
        mn.x = min(mn.x, w.x); mn.y = min(mn.y, w.y); mn.z = min(mn.z, w.z)
        mx.x = max(mx.x, w.x); mx.y = max(mx.y, w.y); mx.z = max(mx.z, w.z)
center = (mn + mx) / 2
diag = (mx - mn).length
print("BBOX", mn.to_tuple(), mx.to_tuple(), "diag=%.1f" % diag)

cam_data = bpy.data.cameras.new("prev_cam")
cam = bpy.data.objects.new("prev_cam", cam_data)
bpy.context.collection.objects.link(cam)
cam.location = center + Vector((0.75, -0.75, 0.55)).normalized() * diag * 1.15
direction = center - cam.location
rot_quat = direction.to_track_quat("-Z", "Y")
cam.rotation_euler = rot_quat.to_euler()
cam_data.lens = 50
cam_data.clip_start = 1.0
cam_data.clip_end = diag * 10

bpy.context.scene.camera = cam
bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
bpy.context.scene.display.shading.light = "STUDIO"
bpy.context.scene.display.shading.color_type = "MATERIAL"
bpy.context.scene.render.resolution_x = 1600
bpy.context.scene.render.resolution_y = 1000
bpy.context.scene.render.filepath = png_path
bpy.context.scene.render.image_settings.file_format = "PNG"
bpy.ops.render.render(write_still=True)
print("PREVIEW_SAVED", png_path)
