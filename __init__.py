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

bl_info = {
    "name" : "NDAA",
    "author" : "Magacaria_Studios",   
    "description" : "First official release by magacaria brought to you by Snaps Development. This addon is all about normal data. Remove, add or alter normal data to your hearts content.",
    "blender" : (2, 83, 7),   
    "version" : (0, 0, 2),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . operator import OT_Operator
from . operator import OT_Operator2
from . operator import OT_Operator3
from . operator import OT_Operator4
from . operator import OT_Operator5
from . panel import ObjectSelectPanel

classes = (OT_Operator, OT_Operator2, OT_Operator3, OT_Operator4, OT_Operator5, ObjectSelectPanel)

register, unregister = bpy.utils.register_classes_factory(classes)
