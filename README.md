<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-daemon-command.svg?maxAge=3600)](https://pypi.org/project/django-daemon-command/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-daemon-command.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-daemon-command.py/actions)

### Installation
```bash
$ [sudo] pip install django-daemon-command
```

#### Pros
+   never stops after exception
    +   exception traceback is saved in the database (`SELECT * FROM daemon_command_exc_traceback`)
+   logs (`SELECT * FROM daemon_command_log`)

##### `settings.py`
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
    <a href="https://readme42.com/">readme42.com</a>
</p>
