from setuptools import setup, find_packages

setup(
    name='weather',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'geopy',
        'PyQt6',
        'requests',
    ],
)