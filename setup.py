import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enrich_omics",                      # This is the name of the package
    version="0.1.8",                     # The initial release version
    author="Sara Masarone",              # Full name of the author
    description="Package to perform enrichment analysis in python using EnrichR and OpenTargets APIs",
    long_description=long_description,   # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(), # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                  # Information to filter the project on PyPi website
    python_requires='>=3.6',            # Minimum version requirement of the package
    py_modules=["enrich_omics"],             # Name of the python package
    package_dir={'':'./'},     # Directory of the source code of the package
    install_requires=['numpy>=1.22.1', 'pandas>=1.0.5', 'altair>=4.1.0', 'requests>=2.24.0', 'mygene>=3.2.2']  # Install other dependencies if any
)
