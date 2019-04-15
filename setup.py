import os
from glob import glob

from setuptools import setup, find_packages

setup(
    name='sockeye-serving',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'sockeye_serving': ['scripts/*']},
    scripts=glob(os.path.join('bin', '*')),
    data_files=[('config', glob(os.path.join('config', '*'))),
                ('notebooks', glob(os.path.join('notebooks', '*')))],
    include_package_data=True
)