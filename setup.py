import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyClassCharts",
    version = "0.0.1",
    author = "Ryan Wiecz",
    author_email = "ryan@ryanwiecz.codes",
    install_requires= ["requests"],
    description = "An unofficial package for interacting with the ClassCharts API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/itsnotrin/PyClassCharts",
    project_urls = {
        "Bug Tracker": "https://github.com/itsnotrin/PyClassCharts/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.7.0"
)