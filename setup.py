from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

install_requires = [
    "aiohttp>=3.12.12,<4",
    "pycryptodome>=3.21.0,<3.22.0",
    "async-class>=0.5.0,<0.6.0",
    "voluptuous>=0.15.2,<0.16.0"
]

setup(
    name="aioremootio",
    version="1.0.0.dev0",
    description="An asynchronous API client library for Remootio (http://www.remootio.com/)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alpha520098/aioremootio",
    author="Gergö Gabor Ilyes-Veisz (modified by alpha520098)",
    author_email="your.email@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.13",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries"
    ],
    keywords="remootio, client, library, asynchronous",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.13",
    install_requires=install_requires,
    project_urls={
        "Bug Tracker": "https://github.com/alpha520098/aioremootio/issues",
        "Source": "https://github.com/alpha520098/aioremootio"
    }
)
