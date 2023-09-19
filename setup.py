from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'PyDId allows developers to easily use the D-ID api without complications.'
LONG_DESCRIPTION = '''The PyDId APIRequest library provides a simplified and convenient way for developers to interact with the D-ID API. With this library, developers can easily integrate D-ID powerful image processing capabilities into their applications without dealing with the complexities of manual API calls.'''

# Setting up
setup(
    name="pyDId",
    version=VERSION,
    author="Ajaga Abdulbasit (Code  Ninja)",
    author_email="basitng2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'ai', 'D-ID',
              'image', 'request', 'video-to-video', 'faceless', 'picture-to-picture'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
