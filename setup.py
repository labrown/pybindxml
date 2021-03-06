from setuptools import setup

# add dependency for python-bs4

setup(
    name='pybindxml',
    version = '0.2',
    description='Read ISC BIND\'s statistics XML for processing.',
    author='Jeffrey Forman',
    author_email='code@jeffreyforman.net',
    license='MIT',
    packages = ['pybindxml'],
    url = 'http:://github.com/jforman/pybindxml',
    install_requires = ['bs4.BeautifulSoup'],
)
