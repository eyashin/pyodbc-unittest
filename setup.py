import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyodbc-unittest",
    version="0.8.7",
    author="Evgeny Yashin",
    author_email="yashin.evgeny@gmail.com",
    description="The library provides SQL calls for the Python unittest framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/eyashin/pyodbc-unittest',  
    project_urls={
        'Bug Reports': 'https://github.com/eyashin/pyodbc-unittest/issues',
        'Source': 'https://github.com/eyashin/pyodbc-unittest/',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
