# issues deploying DRF project to Render due to unrecognised module

DRF project is running in development environment but fails to deploy to Render due to unrecognised module. The error message is as follows:

```
==> Running 'gunicorn core.wsgi:application'
Traceback (most recent call last):
  File "/opt/render/project/src/.venv/bin/gunicorn", line 8, in <module>
    sys.exit(run())
             ^^^^^
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/wsgiapp.py", line 67, in run
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/base.py", line 236, in run
    super().run()
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/base.py", line 72, in run
    Arbiter(self).run()
    ^^^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/arbiter.py", line 58, in __init__
    self.setup(app)
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/arbiter.py", line 118, in setup
    self.app.wsgi()
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
                    ^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
           ^^^^^^^^^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/render/project/src/.venv/lib/python3.11/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'core'
```

gunicorn is called in Procfile as follows:
```Procfile
web: gunicorn core.wsgi:application
```

have tried to change the module name to `django_project.core.wsgi:application` but the error persists.

I have tried to the following project structure:
```
django_project
django_project\core
django_project\core\__pycache__
django_project\core\__init__.py
django_project\core\asgi.py
django_project\core\settings.py
django_project\core\urls.py
django_project\core\wsgi.py # module is defined here? Why can't gunicorn recognise it?
django_project\myapp
django_project\myapp\__pycache__
django_project\myapp\migrations
django_project\myapp\__init__.py
django_project\myapp\admin.py
django_project\myapp\apps.py
django_project\myapp\models.py
django_project\myapp\tests.py
django_project\myapp\urls.py
django_project\myapp\views.py
.env
.gitignore
db.sqlite3
manage.py
Procfile # reads "web: gunicorn core.wsgi:application"
README.md
render.yaml
requirements.txt
```

another potential problem area is yaml file:
```yaml
databases:
  - name: my-database
    plan: free
    region: oregon

services:
  - type: web
    name: my-drf-app
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate"
    startCommand: "gunicorn core.wsgi:application"
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: core.settings
      - key: SECRET_KEY
        generateValue: true
      - key: ALLOWED_HOSTS
        value: my-drf-app.onrender.com
      - key: DATABASE_URL
        value: postgresql://my_database_0jkb_user:oRsLKq[...hidden...]
```

have also tried to change the startCommand to `gunicorn django_project.core.wsgi:application` but the error persists.

can see my full repo here: http://github.com/lmcrean/drf-practise