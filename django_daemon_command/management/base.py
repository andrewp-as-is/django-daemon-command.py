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
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type,exc_value,exc_traceback,file=sys.stderr)

    def save_exception(self,exc):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        f = StringIO()
        traceback.print_exception(exc_type, exc_value, exc_traceback,file=f)
        ExcTraceback(
            pid = os.getpid(),
            command = sys.argv[0],
            type = '.'.join(filter(None,[getattr(exc_type,'__module__',''),exc_type.__name__])),
            value = exc_value if exc_value else '',
            traceback=f.getvalue()
        ).save()

    def process(self,*args, **options):
        raise NotImplementedError('process(self,*args, **options) NOT IMPLEMENTED')

    def log(self,msg):
        if sys.stdout.isatty():
            print('LOG [%s]: %s' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),msg))
        Log(pid = os.getpid(),command = sys.argv[0],msg=msg).save()
