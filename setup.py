from setuptools import setup, find_packages
with open('requirements.txt') as req_file:
    required = req_file.read().splitlines()

setup(name='takehome',
      version='0.1',
      description='',
      author='Michoel Snow',
      author_email='protect3f@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=required
      )
