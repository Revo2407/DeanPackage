from setuptools import setup, find_packages

setup(
    name='package',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Revo2407/DeanPackage',
    author='Dean Roelofse',
    author_email='dean.roelofse@gmail.com'
)
