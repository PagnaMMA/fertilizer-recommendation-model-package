from setuptools import setup, find_packages

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="fertilizer-model",
    version="0.1.0",
    author="Mohamed A. Mouliom Pagna",
    author_email="mohamed.mouliom@aims-cameroon.org",
    description="A machine learning model for fertilizer recommendation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pagnaMMA/fertilizer-recommendation-model-package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "fertilizer_model": ["*.pkl"],
    },
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)