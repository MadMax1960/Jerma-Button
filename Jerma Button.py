bl_info = {
    "name": "Jerma Button",
    "author": "Mudkip",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Adds a Jerma button to the top of the screen",
    "category": "Generic"
}

import bpy

class JermaButtonOperator(bpy.types.Operator):
    bl_idname = "wm.jerma_button_operator"
    bl_label = "Jerma Button"

    def execute(self, context):
        # Object loop
        for obj in bpy.context.scene.objects:
            # Mesh Check
            if obj.type == 'MESH':
                # Vertex group check
                if obj.vertex_groups:
                    # :Grab:
                    mesh = obj.data
                    # Vertex group loop
                    for group in obj.vertex_groups:
                        # Select vertex loop
                        bpy.context.view_layer.objects.active = obj
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.object.vertex_group_set_active(group=group.name)
                        bpy.ops.object.vertex_group_select()

                        # Weight limit please fckign wrok
                        bpy.ops.object.vertex_group_limit_total(limit=4)

                        # Normalize weights
                        bpy.ops.object.vertex_group_normalize_all()

                        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

def draw_jerma_button(self, context):
    layout = self.layout
    layout.operator("wm.jerma_button_operator")

classes = (
    JermaButtonOperator,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.append(draw_jerma_button)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_HT_header.remove(draw_jerma_button)

if __name__ == "__main__":
    register()
