import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snowflake',
    version='0.0.1',
    author='Alex K',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['numpy', 'turtles', 'snowflake'],
    install_requires=['requests'],
)