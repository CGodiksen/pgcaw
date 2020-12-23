import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgcaw",
    version="0.0.1",
    author="Christian Godiksen",
    author_email="christian.godiksen55@gmail.com",
    description="PGCAW is a very simple API wrapper for the github contributions calendar.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CGodiksen/pgcaw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)