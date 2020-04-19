from setuptools import setup

setup(
    name='django-daemon-command',
    version='2020.4.20',
    install_requires=[
        'Django',
        'setuptools',
    ],
    packages=[
        'django_daemon_command',
        'django_daemon_command.management',
        'django_daemon_command.migrations',
    ],
)
