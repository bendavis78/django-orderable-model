from setuptools import setup, find_packages

setup(
    name='django-orderable-model',
    version='0.1-dev',
    test_suite='orderable.test',
    packages=find_packages(),
    install_requires=[],
    package_data={'orderable': []}
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.rst').read(),
)
