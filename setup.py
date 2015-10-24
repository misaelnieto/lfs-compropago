from setuptools import setup, find_packages

setup(
    name = 'lfs-compropago',
    description = 'ComproPago payment processor for LFS',
    version = '0.1',
    packages = find_packages(),
    author = 'Noe Nieto',
    author_email = 'nnieto@noenieto.com',
    license = 'MIT',
    url = 'http://github.io/tzicatl/lfs-compropago',
    install_requires = ['compropago-python','python-dateutil'],
    tests_require = ['nose>=1.0', 'responses'],
)
