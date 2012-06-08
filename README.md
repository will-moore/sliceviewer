sliceviewer
===========

EMDB-customised viewer for OMERO.web framework

cd components/tools/OmeroWeb/omeroweb/
git clone git://github.com/will-moore/sliceviewer.git
path/to/bin/omero config set omero.web.apps '["sliceviewer"]'

cd sliceviewer
# you are now in the new 'sliceviewer' git repository
git status


# Enable public access to a specific account
path/to/bin/omero config set omero.web.public.enabled True
path/to/bin/omero config set omero.web.public.user <username>
path/to/bin/omero config set omero.web.public.password <password>