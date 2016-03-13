from os.path import join, dirname

import pylemm
from setuptools import setup, find_packages

setup(
        name="program",
        version=pylemm.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=['nltk', ],
        entry_points={
            'console_scripts':
                ['program = program.script:main']
        }

)
