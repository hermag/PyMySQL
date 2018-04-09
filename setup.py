"""Importing setup for settingup the package."""
from setuptools import setup


def readme():
    """Provide README for the package."""
    with open('README.rst') as f:
        return f.read()


setup(name='pymysql',
      version='0.1',
      description='Library to control and manage, MySQL database and its tables.',
      long_description='Library with vast functionality for management and control of the MySQL database and its tables.',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Database :: Database Operations',
          "Operating System :: Linux",
      ],
      keywords='MySQL SELECT INSERT UPDATE CREATE TABLE',
      url='http://github.com/hermag/PyMySQL',
      download_url='https://github.com/hermag/PyMySQL/archive/master.zip',
      author='Erekle Magradze',
      author_email='erekle@magradze.de',
      license='MIT',
      # install_requires=[
      #"os",
      # subprocess
      #],
      packages=['pymysql'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
