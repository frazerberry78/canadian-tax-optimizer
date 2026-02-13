from setuptools import setup, find_packages

setup(
    name='canadian-tax-optimizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # list dependencies here
    ],
    entry_points={
        'console_scripts': [
            'tax-optimizer=your_module:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)