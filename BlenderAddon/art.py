# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The Original Code is Copyright (C) 2017 Marcelo "Tanda" Cerviño. 
# http://lodetanda.blogspot.com/ 
# All rights reserved.
#
# Contributor(s):
#
# ***** END GPL LICENCE BLOCK *****

bl_info = { 
    "name": "ART -Approximate Render Time Calculator-",
    "author": "Marcelo 'Tanda' Cerviño",
    "version": (1, 0),
    "blender": (2, 78),
    "location": "Render > ART -Approx Render Time-",
    "description": "Approximate Render Time Calculator",
    "warning": "",
    "wiki_url": "https://github.com/eLeDeTe-LoDeTanda/ART",
    "tracker_url": "https://github.com/eLeDeTe-LoDeTanda/ART/issues",
    "category": "Render",
}

import bpy
from bpy.props import IntProperty, PointerProperty
from bpy.types import PropertyGroup, Operator, Panel

###########################################################


class artPanel(Panel):
    bl_label = "ART -Approx Render Time-"
    bl_idname = "RENDER_PT_ART"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        ani_duration = scene.art.frames / scene.art.fps;
        
        time = ((scene.art.frames * (((scene.art.hours * 60) + scene.art.minutes) * 60 + scene.art.seconds)) / scene.art.cpu);
        
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
        row.prop(scene.art, "hours")
        row.prop(scene.art, "minutes")
        row.prop(scene.art, "seconds")
        
        row = col.row()
        
        row.label("Frames and rate:")
        row = col.row(align=True)
        row.prop(scene.art, "frames")
        row.prop(scene.art, "fps")
        
        row = col.row(align=True)
        row.prop(scene.art, "cpu")


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
    bpy.types.Scene.art = PointerProperty(type=artProperty)

def unregister():
    del(bpy.types.Scene.art)
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
