import os
import setuptools
from setuptools import setup
import version

requirements = list(open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r').readlines())

print(setuptools.find_packages('src'))

setup(name='python-tds-dbrs',
      version=version.get_git_version(),
      description='DBRS fork of Python DBAPI driver for MSSQL using pure Python TDS (Tabular Data Stream) protocol implementation with some critical fixes not yet merged or released in mainline pytds.',
      author='Mikhail Denisenko',
      author_email='denisenkom@gmail.com',
      url='https://github.com/denisenkom/pytds',
      license="MIT",
      packages=['pytds'],
      package_dir={'': 'src'},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          "Private :: Do Not Upload"  # Makes PyPI reject upload if someone accidentally attempts to upload to PyPI
      ],
      zip_safe=True,
      install_requires=requirements,
      )
