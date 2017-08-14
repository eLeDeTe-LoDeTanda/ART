import bpy
from bpy.props import IntProperty, PointerProperty
from bpy.types import PropertyGroup, Operator, Panel

bl_info = { 
    "name": "ART -Aproximate Render Time Calculator-",
    "author": "Marcelo 'Tanda' Cerviño",
    "version": (1, 0),
    "blender": (2, 78),
    "location": "Render > ART -Aprox Render Time-",
    "description": "Aproximate Render Time Calculator",
    "warning": "",
    "wiki_url": "https://github.com/eLeDeTe-LoDeTanda/ART",
    "tracker_url": "https://github.com/eLeDeTe-LoDeTanda/ART/issues",
    "category": "Render",
}


###########################################################


class artPanel(Panel):
    bl_label = "ART -Aprox Render Time-"
    bl_idname = "RENDER_PT_ART"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        ani_duration = scene.ART.frames / scene.ART.fps;
        
        #if (scene.ART.cpu > scene.ART.frames):
        #scene.ART.cpu = scene.ART.frames
       
        time = ((scene.ART.frames * (((scene.ART.hours * 60) + scene.ART.minutes) * 60 + scene.ART.seconds)) / scene.ART.cpu);
        
        s = time % 60
        m = time / 60
        h = m / 60
        m = m % 60
        d = h / 24
        h = h % 24

        anis = ani_duration % 60
        anim = ani_duration / 60
        anih = anim / 60
        anim = anim % 60
        
        layout.label(text="ANIMATION:")
        box = layout.box()
        box.label(text="{}h:  {}m:  {}s".format(int(anih), int(anim), int(anis)))

        layout.label(text="RENDER TIME:") 
        box = layout.box()
        box.label(text="{}d:  {}h:  {}m:  {}s".format(int(d), int(h), int(m), int(s))) 

        col = layout.column(align=True)
        row = col.row()
        
        row.label("Time per frame:")
        row = col.row()
        row.prop(scene.ART, "hours")
        row.prop(scene.ART, "minutes")
        row.prop(scene.ART, "seconds")
        
        row = col.row()
        
        row.label("Frames and rate:")
        row = col.row(align=True)
        row.prop(scene.ART, "frames")
        row.prop(scene.ART, "fps")
        
        row = col.row(align=True)
        row.prop(scene.ART, "cpu")


class artProperty(PropertyGroup):
    hours = IntProperty(
        name="H",
        min=0,
        default=0
    )
    minutes = IntProperty(
        name="M",
        min=0,
        max=60,
        default=0
    )
    seconds = IntProperty(
        name="S",
        min=0,
        max=60,
        default=0
    )
    frames = IntProperty(
        name="Frames",
        min=1,
        max=9999999,
        default=250
    )
    fps = IntProperty(
        name="fps",
        min=1,
        max=999,
        default=24
    )
    cpu = IntProperty(
        name="CPUs",
        min=1,
        max=9999999,
        default=1
    )
    
###########################################################
        
def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.ART = PointerProperty(type=artProperty)

def unregister():
    del(bpy.types.Scene.ART)
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()