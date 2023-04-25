from os import environ

import django_stubs_ext
from split_settings.tools import include, optional
from password_generator.settings.components import config
# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

# Managing environment via `DJANGO_ENV` variable:
_ENV = config('DJANGO_ENV')

_base_settings = (
    'components/common.py',
    'components/logging.py',
    'components/csp.py',
    'components/caches.py',

    # Select the right env:
    'environments/{0}.py'.format(_ENV),

    # Optionally override some settings:
    optional('environments/local.py'),
)

# Include settings:
include(*_base_settings)