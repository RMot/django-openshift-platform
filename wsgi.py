#!/usr/bin/python
import os
import sys

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

# add the virtualenv site-packages path to the sys.path
sys.path.append(os.path.join(virtenv, 'lib64/python2.7/site-packages'))

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from plataforma.plataforma.wsgi import baseapp
