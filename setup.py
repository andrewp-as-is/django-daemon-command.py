import setuptools

setuptools.setup(
    name='django-daemon-command',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
