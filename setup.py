from setuptools import setup

setup(
    name='transparent-image-generator',
    version='0.0.1',
    url='https://github.com/coint-hub/transparent-image-generator',
    packages=['transparent_image_generator'],
    install_requires=['pypng>=0.0.20'],
    extras_require={'dev': ['pytest']}
)
