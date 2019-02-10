from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='itunesdiff',
      version=version,
      description="Diffs two iTunes XML files",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='iTunes diff',
      author='Sebastian Hojas',
      author_email='later@irrelevant.at',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "libpytunes >= 1.0.1"
      ],
      entry_points = {
          "console_scripts": ['itunesdiff = itunesdiff.__main__:main']
      },
      )
