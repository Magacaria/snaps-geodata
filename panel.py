import bpy
from bpy.props import IntProperty, PointerProperty
from bpy.types import Panel, PropertyGroup, Operator
import random

class ObjectSelectPanel(bpy.types.Panel):
    bl_idname = "SnapsPanel4"
    bl_label = ""   
    bl_category = "Snaps" 
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"   

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="SNAPS | GeoSettings")

    def draw(self, context):
        layout = self.layout       
        box = layout.box()

        box.label(text=" SNAPS | Imported Data")
        box.operator('view3d.autosmooth', text="Clear Custom Normals")    

        box = layout.box()
        box.label(text=" SNAPS | Geodata Normals")
        box.operator('view3d.autosmoothapply', text=" Auto Smooth")
        box.operator('view3d.viewnormals', text=" Visualise Normals - True")
        box.operator('view3d.viewnormalsfalse', text="Visualised Normals - False")

        box = layout.box()
        box.label(text=" SNAPS | Geodata Culling")
        box.operator('view3d.viewbackfacecull', text="Backface Culling")

        box = layout.box()
        box.label(text=" SNAPS | Custom Commands")
 
        box = layout.box()
        box.label(text=" Provided by Magacaria Studios")
        
