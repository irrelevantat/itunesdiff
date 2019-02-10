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
      url='https://github.com/Sebastian-Hojas/itunesdiff',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "libpytunes"
      ],
      python_requires="=2.7",
      entry_points = {
          "console_scripts": ['itunesdiff = itunesdiff.__main__:main']
      },
      dependency_links = ['git://github.com/liamks/libpytunes@26b48c5#egg=libpytunes']
      )
