from django.db import models

class ExcTraceback(models.Model):
    pid = models.IntegerField()
    argv = models.TextField()
    type = models.TextField()
    value = models.TextField()
    traceback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'daemon_command_exc_traceback'


class Log(models.Model):
    pid = models.IntegerField()
    argv = models.TextField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'daemon_command_log'
