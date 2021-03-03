from setuptools import setup, find_packages

setup(name='ftfinder',
      description='The easy way to find TODO and FINDME annotations in your project.',
      author='Miłosz Hoć',
      author_email='miloszhoc@gmail.com',
      version=str(1.1),
      packages=find_packages(exclude=['tests', 'venv']),

      py_modules=['ftfinder'],
      entry_points={'console_scripts': ['ftfinder = ftfinder:main', ]},
      )
