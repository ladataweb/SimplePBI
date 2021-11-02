from setuptools import find_packages, setup

classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
]

setup(
    name='SimplePBI',
    packages=find_packages(),
    version='0.0.2',
    download_url='',
    url='',
    description='Simplify usage of Power Bi Admin API',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    author='Martin Zurita <martinzurita1@gmail.com>, Ignacio Barrau <igna_barrau@hotmail.com>',
    license='MIT',
    classifiers=classifiers,
    install_requires=[
        'requests', 
        'pandas'
    ],
    keywords=['Power BI', 'Azure', 'Data']
)
