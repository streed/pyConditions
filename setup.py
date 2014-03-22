from distutils.core import setup

setup(
    name='pyConditions',
    version='0.3.0',
    author='Sean Reed',
    author_email='streed@mail.roanoke.edu',
    packages=['pyconditions', 'pyconditions.test'],
    url='http://github.com/streed/pyConditions',
    license='LICENSE.txt',
    description='Commenting sucks so let your code do it for you with Guava like preconditions that also actually do something.',
    long_description=open('README.rst').read(),
)
