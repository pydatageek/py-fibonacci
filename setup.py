import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-fibonacci",
    version="0.5.2",
    author="Haluk Aksu",
    author_email="pydatageek@gmail.com",
    description="Generates Fibonacci series with an end number OR a length argument.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pydatageek/py-fibonacci",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.6',
)
