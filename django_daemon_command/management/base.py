from datetime import datetime
import os
import sys
import time
import traceback

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.core.management.base import BaseCommand

from django_daemon_command.models import Log, ExcTraceback



class DaemonCommand(BaseCommand):
    sleep = 5

    def handle(self, *args, **options):
        self.daemonize(*args, **options)

    def daemonize(self, *args, **options):
        while True:
            try:
                self.process(*args, **options)
            except Exception as exc:
                self.on_exception(exc)
            finally:
                time.sleep(self.sleep)

    def on_exception(self,exc):
        self.print_exception(exc)
        self.save_exception(exc)

    def print_exception(self,exc):
        traceback.print_exception(type(exc),str(exc),exc.__traceback__,file=sys.stderr)

    def save_exception(self,exc):
        f = StringIO()
        traceback.print_exception(type(exc), str(exc), exc.__traceback__,file=f)
        type = exc.__module__+'.'+exc.__name__ if exc.__module__ else exc.__name__
        ExcTraceback(
            pid = os.getpid(),
            argv = ' '.join(sys.argv),
            type = exc.__module__+'.'+exc.__name__ if exc.__module__ else exc.__name__,
            value = exc_value if value else '',
            traceback=f.getvalue()
        ).save()

    def process(self,*args, **options):
        raise NotImplementedError('process(self,*args, **options) NOT IMPLEMENTED')

    def log(self,msg):
        if sys.stdout.isatty():
            print('LOG [%s]: %s' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),msg))
        Log(pid = os.getpid(),argv=' '.join(sys.argv),msg=msg).save()
