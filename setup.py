from setuptools import find_packages, setup
setup (
    name='ctof',
    packages=find_packages(include=['ctof']),
    version='0.2.01',
    description='A simple library for temperature unit conversion',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='David Costell',
    author_email = 'davidcostell44@gmail.com',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    project_urls = {
        'GitHub': 'https://github.com/DontEatThemCookies/ctof'
        }
)
