from setuptools import setup, find_packages

setup(
    name='Syumi-note',
    version='0.1.0',
    description='Learning something',
    author='Yuki Ichihara',
    author_email='y.ichihara3406@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.2',
        'scipy==1.10.0',
        'matplotlib==3.6.3',
        'jax==0.4.2'
        'pulp==2.4.0'
    ],
)
