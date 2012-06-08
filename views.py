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

from django.core.urlresolvers import reverse

from omeroweb.webclient import webclient_gateway
from omeroweb.decorators import login_required
from omeroweb.webgateway import views as webgateway_views

#from omeroweb.feedback.views import handlerInternalError


def index(request):
    return Http404("Sliceviewer index page not supported")


@login_required()
def sliceviewer (request, emdb_entry, conn=None, **kwargs):
    """ We need handle one, multiple, and no match on the image_name """

    image_name = "emd_%s.map" % emdb_entry
    images = conn.getObjects("Image", attributes={'name': image_name})

    id = -1
    image = None
    for image in images:
        if image.getId() > id: 
            id = image.getId()
        
    if image is None:
        logger.debug('sliceviewer: No Image named %s' % image_name)
        raise Http404

    kwargs['viewport_server'] = reverse('emdbindex')
    kwargs['template'] = 'sliceviewer/sliceviewer.html'
    return webgateway_views.full_viewer(request, image.id, _conn=conn, **kwargs)
