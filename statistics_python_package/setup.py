from setuptools import setup

setup(
    name='statistics_python_package',
    version='0.2',  # Increment the version number
    description='A package for Gaussian and Binomial distributions',
    author='Chilakala Naveen Kumar',
    author_email='naveen.chilakala@gmail.com',
    install_requires=[
      'matplotlib>=3.9.1.post1',
      'numpy>=2.0.1',
      'scipy>=1.14.0'
    ]
)
