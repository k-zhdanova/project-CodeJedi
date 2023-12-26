from setuptools import setup, find_packages

setup(
    name="codejedi",
    description="Galactic Address Book",
    version="0.1.0",
    url="https://github.com/k-zhdanova/project-CodeJedi",
    author="project-group-4",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",],
    include_package_data=True,
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "main = codejedi:main"
        ]
    }
)