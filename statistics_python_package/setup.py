from setuptools import setup

setup(
    name='gaussian_binomial_distributions',
    version='1',  # Increment the version number
    description='A package for Gaussian and Binomial distributions',
    author='Chilakala Naveen Kumar',
    author_email='naveen.chilakala@gmail.com',
    packages=['gaussian_binomial_distributions'],
    install_requires=[
      'matplotlib>=3.9.1.post1',
      'numpy>=2.0.1',
      'scipy>=1.14.0'
    ]
)
