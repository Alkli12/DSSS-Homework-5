import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snowflakecreate',
    version='0.0.1',
    author='Alex K',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['snowflakecreate'],
    install_requires=['requests'],
)