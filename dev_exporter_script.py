import bpy
import os

savingPath = 'F:\\infographie\\dev\\blenderscript\\dev_exporter\\'
nameFbx = bpy.context.selected_objects
#nameFbx = bpy.context.visible_objects

if len(nameFbx) > 0:
    name = nameFbx[0].id_data.name

nameOfObjetcs = [o.name for o in nameFbx]
print("L'array est == ", nameOfObjetcs)

for obj2Export in nameOfObjetcs :
    
    print("Premier print FOR == ",obj2Export)
    
    # select the object
    obj = bpy.data.objects[obj2Export]
    
    print("Second print FOR == ", obj)
    
    bpy.context.scene.objects.active = obj
    
    # look if object have FBX inside it name
    if "fbx" in obj2Export:
        print("C'est un fbx")
        bpy.ops.export_scene.fbx(filepath=savingPath + str(obj2Export) + ".fbx", axis_forward='-Z', axis_up='Y', use_selection=True)
    
    
    
    else :
        print("---------------")
        
        bpy.ops.export_scene.autodesk_3ds(filepath= savingPath + str(obj2Export) + "_props" + ".3ds", check_existing=True, 
        axis_forward='Y', axis_up='Z', filter_glob="*.3ds", use_selection=True)
        
        bpy.ops.export_scene.obj(filepath= savingPath + str(obj2Export) + "_props" + ".obj", check_existing=True, 
        axis_forward='Y', axis_up='Z', filter_glob="*.obj", use_materials=False, use_selection=True)
        