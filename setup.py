from setuptools import find_packages
from setuptools import setup

try:
    with open('.version') as f:
        VERSION = f.readline().strip()
except IOError:
    VERSION = 'unknown'

setup(
    name='ocfweb',
    version=VERSION,
    packages=find_packages(exclude=['debian', 'venv']),
    include_package_data=True,
    url='https://www.ocf.berkeley.edu/',
    author='Open Computing Facility',
    author_email='help@ocf.berkeley.edu',
    install_requires=[
        'cached-property',
        'celery[redis]',
        'django-bootstrap-form',
        'django-ipware',
        'django-mathfilters',
        'django-redis',
        'django>=1.10,<1.10.999',
        'gunicorn',
        'libsass',
        'matplotlib',
        'mistune',
        'numpy',
        'ocflib',
        'pycrypto',
        'pygments',
        'pymysql',
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'ocfweb-run-periodic-functions = ocfweb.bin.run_periodic_functions:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
