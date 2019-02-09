from setuptools import setup

setup(
    name='itunesdiff',
    version='0.1.0',
    author='Sebastian Hojas',
    author_email='later@irrelevant.at',
    packages=['itunesdiff'],
    url='https://pypi.python.org/pypi/itunesdiff/',
    license='LICENSE.txt',
    description='Makes sense of two iTunes XML files',
    long_description=open('README.md').read(),
    install_requires=[
        "pyitunes >= 1.0.1",
    ],
    entry_points = {
        "console_scripts": ['notevault = notevault.__main__:main']
    },
)
