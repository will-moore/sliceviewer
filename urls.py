#!/usr/bin/env python
# 
# Copyright (c) 2008-2012 University of Dundee.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls.defaults import patterns, url

from omeroweb.sliceviewer import views
from omeroweb.webgateway import views as webgateway_views

urlpatterns = patterns('django.views.generic.simple',

    # we use this within javascript to generate full paths
    url( r'^$', views.index, name="emdbindex" ),

    # tomogram viewer (customised Image Viewer for single T and C)
    url( r'^(?P<emdb_entry>\d{4})_sliceviewer/$', views.sliceviewer, name='webemdb_sliceviewer' ),
    url ( r'^imgData/(?P<iid>[^/]+)/(?:(?P<key>[^/]+)/)?$', webgateway_views.imageData_json ),
    url( r'^render_image/(?P<iid>[0-9]+)/(?P<z>[0-9]+)/(?P<t>[0-9]+)/$', webgateway_views.render_image, name="emdb_render_image"),

)