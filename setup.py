import re
import setuptools

version_file = 'devito_rtm/_version.py'
version_line = open(version_file, 'r').read()
version_re = r'^__version__ = ["\']([^"\']*)["\']'
mo = re.search(version_re, version_line, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError(f'Unable to find version string in {version_file}.')

def configure():
# Initialize the setup kwargs
    kwargs = {
            'name': 'Devito-RTM',
            'version': version,
            'author': 'Malcolm C. A. White',
            'author_email': 'malcolmw@mit.edu',
            'maintainer': 'Malcolm C. A. White',
            'maintainer_email': 'malcolmw@mit.edu',
            'url': 'http://malcolmw.github.io/Devito-RTM',
            'description': 'Reverse-time migration scripts for '
                'detecting/locating earthquakes using Devito.',
            'download_url': 'https://github.com/malcolmw/Devito-RTM.git',
            'platforms': ['linux'],
            'install_requires': ['devito', 'numpy', 'pandas'],
            'packages': ['devito_rtm']
            }
    return kwargs

if __name__ == '__main__':
    kwargs = configure()
    setuptools.setup(**kwargs)
