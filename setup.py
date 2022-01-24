import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbt_dimes",
    version="0.0.1",
    author="Dave Coulter",
    author_email="dave.coulter@rmit.edu.au",
    description="Functions to help build dbt models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pandas', 
    packages = setuptools.find_packages()
)
