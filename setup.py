from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kin',
    version='2.0.2',
    description='A simple project.pbxproj verifier',
    long_description=long_description,
    url='https://github.com/Karumi/Kin',
    author='Karumi',
    author_email='tech@karumi.com',
    license='Apache Software',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],

    keywords='xcode project.pbxproj lint objective-c swift ios',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'argparse==1.4.0',
        'antlr4-python3-runtime==4.9.2'
    ],
    entry_points={
        'console_scripts': [
            'kin = kin.kin:main',
        ],
    },
)
