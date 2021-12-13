import bpy
import bmesh

bl_info = {
    "name": "Toggle Seam & Sharp",
    "blender": (3, 0, 0),
    "category": "Object",
}

class MeshToggleSeam(bpy.types.Operator):
    """Toggle Seam"""
    bl_idname = "edge.toggle_seam"
    bl_label = "Toggle Seam"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            if obj.mode != 'EDIT':
                break
            bm = bmesh.from_edit_mesh(obj.data)
            
            for e in bm.edges:
                if e.select:
                    e.seam = not e.seam

            obj.data.update()

        return {'FINISHED'}
    
class MeshToggleSharp(bpy.types.Operator):
    """Toggle Sharp"""
    bl_idname = "edge.toggle_sharp"
    bl_label = "Toggle Sharp"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            if obj.mode != 'EDIT':
                break
            bm = bmesh.from_edit_mesh(obj.data)
            
            for e in bm.edges:
                if e.select:
                    e.smooth = not e.smooth

            obj.data.update()

        return {'FINISHED'}

def seam_menu_func(self, context):
    self.layout.operator(MeshToggleSeam.bl_idname)
    
def sharp_menu_func(self, context):
    self.layout.operator(MeshToggleSharp.bl_idname)
    
def register():
    bpy.utils.register_class(MeshToggleSeam)
    bpy.utils.register_class(MeshToggleSharp)
    bpy.types.VIEW3D_MT_edit_mesh.append(seam_menu_func)
    bpy.types.VIEW3D_MT_edit_mesh.append(sharp_menu_func)
    
def unregister():
    bpy.utils.unregister_class(MeshToggleSeam)
    bpy.utils.unregister_class(MeshToggleSharp)
