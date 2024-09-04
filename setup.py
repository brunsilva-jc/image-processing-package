from distutils.command.install import install

from setuptools import setup, find_packages

with open("README.md", "r")as file:
    project_description = file.read()

with open("requirements.txt", "r")as file:
    requirements = file.read().splitlines()


setup(
    name="image_processing_brunsilvajc",
    version="0.0.2",
    author="BrunSilva-JC",
    author_email="brunsilva.jc@gmail.com",
    description="package for processing images",
    long_description=project_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brunsilva-jc/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.10"
)