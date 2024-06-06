from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='DockerKube',
    version='0.1',
    packages=find_packages(),
    author='Pirate-Emperor',
    install_requires=required
)