import bpy 
import math

class OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.autosmooth"
    bl_label = "Clear Custom Normals - Self"
    bl_description = "Clears custom split normal data on selected objects."

    def execute(self, context):
        selection = bpy.context.selected_objects
        for o in selection:
            bpy.context.view_layer.objects.active = o
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
        return {'FINISHED'}

class OT_Operator2(bpy.types.Operator):
    bl_idname = "view3d.autosmoothapply"
    bl_label = "Enables Auto Smooth"
    bl_description = "Applies auto smooth on a 30 degree angle (0.523599 radians) to selected objects"

    def execute(self, context):
        selection2 = bpy.context.selected_objects

        for o in selection2:
            bpy.context.view_layer.objects.active = o
            bpy.ops.object.shade_smooth()
            bpy.context.object.data.use_auto_smooth = True
            # In radians.
            bpy.context.object.data.auto_smooth_angle = 0.523599
        return {'FINISHED'}

class OT_Operator3(bpy.types.Operator):
    bl_idname = "view3d.viewbackfacecull"
    bl_label = "Backface Culling"
    bl_description = "Toggles backface culling"

    def execute(self, context):
        bpy.context.space_data.shading.show_backface_culling = True
        return {'FINISHED'}       

class OT_Operator4(bpy.types.Operator):
    bl_idname = "view3d.viewnormals"
    bl_label = "View Normals"
    bl_description = "Toggles normal overlay"  

    def execute(self, context): 
        bpy.context.space_data.overlay.show_vertex_normals = True
        bpy.context.space_data.overlay.show_split_normals = True
        bpy.context.space_data.overlay.show_face_normals = True
        bpy.context.space_data.overlay.normals_length = 0.5   
        return {'FINISHED'}

class OT_Operator5(bpy.types.Operator):
    bl_idname = "view3d.viewnormalsfalse"
    bl_label = "View Normals"
    bl_description = "Toggles normal overlay"  

    def execute(self, context): 
        bpy.context.space_data.overlay.show_vertex_normals = False
        bpy.context.space_data.overlay.show_split_normals = False
        bpy.context.space_data.overlay.show_face_normals = False
        bpy.context.space_data.overlay.normals_length = 0.5
        return {'FINISHED'}
            