<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-daemon-command.svg?longCache=True)](https://pypi.org/project/django-daemon-command/)
[![](https://img.shields.io/pypi/v/django-daemon-command.svg?maxAge=3600)](https://pypi.org/project/django-daemon-command/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-daemon-command.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-daemon-command.py/)

#### Installation
```bash
$ [sudo] pip install django-daemon-command
```

#### Pros
+   never stops after exception
    +   exception traceback is saved in the database (`SELECT * FROM daemon_command_exc_traceback`)
+   logs (`SELECT * FROM daemon_command_log`)

#### Settings
```python
INSTALLED_APPS = [
    ...
    'django_daemon_command',
    ...
]
```

```bash
$ python manage.py migrate
```

#### Examples
`app/management/commands/command.py`
```python
from django_daemon_command.management.base import DaemonCommand

class Command(DaemonCommand):
    sleep = 5

    def process(self,*args,**options):
        self.log('msg') # SELECT * FROM daemon_command_log
```

```bash
$ python manage.py command
```

customize
```python
class Command(DaemonCommand):
    def handle(self, *args, **options):
        ... # init
        self.daemonize(*args, **options)

    def on_exception(self,exc):
        self.print_exception(exc)
        self.save_exception(exc)
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>