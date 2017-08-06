# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Acysos S.L. (http://acysos.com) All Rights Reserved.
#                       Ignacio Ibeas <ignacio@acysos.com>
#                       Daniel Pascal <daniel@acysos.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Real Estate Web Common",
    "version" : "1.0",
    "author" : "Acysos S.L.",
    "website" : "www.acysos.com",
    "description": """Common information for internet website and portals""",
    "license" : "AGPL-3",
    "category" : "Specific Industry Applications",
    "depends" : [
        "base",
        "real_estate_base",
        "real_estate_publication",
#        "smile_export",
#        "smile_export_file",
#        "acy_smile_export_file_extended",
        ],
    "init_xml" : [],
    "demo_xml" : [],
    "data" :[
        'views/top_view.xml',
        ],
    "active": False,
    "installable": True
}