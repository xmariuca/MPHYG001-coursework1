from setuptools import setup, find_packages
setup(
    name = "Greengraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/getGreenGraph'],
    install_requires = [
        'argparse',
        'matplotlib',
        'geopy',
        'numpy'
        ]
)
