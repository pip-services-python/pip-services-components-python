"""
Pip.Services Components
--------------------

Pip.Services is an open-source library of basic microservices.
pip_services_components package provides basic abstractions portable across variety of languages.

Links
`````

* `website <http://github.com/pip-services-python/pip-services-components-python>`
* `development version <http://github.com/pip-services-python/pip-services-components-python>`

"""

from setuptools import setup
from setuptools import find_packages

setup(
    name='pip_services_components',
    version='3.0.0',
    url='http://github.com/pip-services-python/pip-services-components-python',
    license='MIT',
    description='Basic portable abstractions for Pip.Services in Python',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    long_description=__doc__,
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'iso8601', 'PyYAML', 'pystache', 'pip_services_commons'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)
