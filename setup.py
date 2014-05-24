from distutils.core import setup

setup(
    name='pyConditions',
    version='0.5.0',
    author='Sean Reed',
    author_email='streed@mail.roanoke.edu',
    packages=['pyconditions', 'pyconditions.test'],
    url='http://github.com/streed/pyConditions',
    license='LICENSE.txt',
    description='Commenting sucks so let your code do it for you with Guava like preconditions that also actually do something.',
    long_description=open('README.rst').read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "License :: OSI Approved :: Apache Software License",
      "Programming Language :: Python :: 2.6",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3.2",
      "Programming Language :: Python :: 3.3",
      "Programming Language :: Python :: Implementation :: CPython",
      "Programming Language :: Python :: Implementation :: PyPy",
      "Topic :: Software Development :: Quality Assurance"
    ],
)
