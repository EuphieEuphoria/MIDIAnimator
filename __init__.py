# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

if "bpy" in locals():
    # Running under Blender
    import importlib
    importlib.reload(src)
    importlib.reload(utils)
    importlib.reload(ui)

else:
    # Running under external instance
    import bpy
    from . src import *
    from . utils import *
    from . ui import *
    from . ui.test_op import TEST_OT_my_operator
    from . ui.test_panel import TEST_PT_my_panel

import bpy

bl_info = {
    "name": "MIDI Animator",
    "author": "iMac",
    "description": "Animate objects with MIDI.",
    "blender": (2, 91, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}


classes = (TEST_OT_my_operator, TEST_PT_my_panel)

register, unregister = bpy.utils.register_classes_factory(classes)
