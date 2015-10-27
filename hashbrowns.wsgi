# for use with mod_wsgi, though it might actually work with uWSGI as well.
# Will test that with nginx at a later date.

import sys
# patch in /path/to/application
sys.path.insert(0, '/var/www/hashbrowns/')

from www import app as application
