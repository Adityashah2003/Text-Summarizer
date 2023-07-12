from setuptools import setup, find_packages

with open('requirements.txt' , 'r') as file:
    requirements = [line for line in file.read().split('/n')]

setup(
    name='summarizer',
    version='1.0.0',
    author='Flamethrowerp',
    author_email='adityashah6020@email.com',
    description='Python Tool to summarize your text',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'summarizer = summarize.main:main',
        ],
    },
)
