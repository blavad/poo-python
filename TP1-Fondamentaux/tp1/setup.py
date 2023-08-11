from setuptools import setup, find_packages

print(find_packages())

setup(
    name='tp1',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    install_requires=['numpy >= 1.11.1'],
    # packages=find_packages(),    
    packages=['tp1', 'tp1.math'],
)