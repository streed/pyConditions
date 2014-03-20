from distutils.core import setup

setup(
    name='pyConditions',
    version='0.1.0',
    author='Sean Reed',
    author_email='streed@mail.roanoke.edu',
    packages=['pyconditions', 'pyconditions.test'],
    url='http://github.com/streed/pyConditions',
    license='LICENSE.txt',
    description='Guava Preconditions in Python.',
    long_description=open('README.rst').read(),
)
