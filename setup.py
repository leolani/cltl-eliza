from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()

setup(
    name='cltl.eliza',
    version=version,
    package_dir={'': 'src'},
    packages=find_namespace_packages(include=['cltl.*', 'cltl_service.*'], where='src'),
    data_files=[('VERSION', ['VERSION'])],
    url="https://github.com/leolani/cltl-eliza",
    license='MIT License',
    author='CLTL',
    author_email='t.baier@vu.nl',
    description='Eliza component for Leolani',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    install_requires=['cltl.combot', 'emissor'],
    extras_require={
        "service": [
            "cltl.emissor-data",
        ]}
)