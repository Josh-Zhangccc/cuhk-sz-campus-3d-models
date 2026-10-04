import bpy
import sys
import time

scene_name = sys.argv[-1]
root = r"D:/My Programs/Unity Programs/cuhk_sz_models_backup"
gltf_path = root + "/gltf_export/" + scene_name + "/" + scene_name + ".gltf"
blend_path = root + "/gltf_export/" + scene_name + "/" + scene_name + ".blend"

t0 = time.time()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=gltf_path)

mesh_objs = [o for o in bpy.data.objects if o.type == "MESH"]
verts = sum(len(o.data.vertices) for o in mesh_objs)
faces = sum(len(o.data.polygons) for o in mesh_objs)
images = [i for i in bpy.data.images if i.size[0] > 0]
img_mem = sum(i.size[0] * i.size[1] * (4 if i.channels == 4 else i.channels) for i in images)
packed = sum(1 for i in images if i.packed_file)

print("BLENDER_CHECK name=%s meshes=%d verts=%d faces=%d images=%d packed=%d import_time=%.0fs"
      % (scene_name, len(mesh_objs), verts, faces, len(images), packed, time.time() - t0))

bpy.ops.wm.save_as_mainfile(filepath=blend_path, compress=True)
print("BLENDER_SAVED %s (%.1f MB on disk)" % (blend_path, __import__("os").path.getsize(blend_path) / 1e6))
