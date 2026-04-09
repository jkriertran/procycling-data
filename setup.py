
from setuptools import setup, find_packages

setup(
    name='procycling_data',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'procycling_data': ['data/raw/procycling_proteam_analysis/**/*.md'],
    },
    install_requires=[
        # List your project dependencies here
        # 'pandas',
        # 'numpy',
    ],
    author='Manus AI',
    author_email='manus-ai@example.com',
    description='A collection of procycling datasets for analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jkriertran/procycling-data',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
