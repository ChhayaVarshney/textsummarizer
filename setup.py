from setuptools import setup, find_packages
from typing import List

with open("README.md", "r") as f:
    long_description = f.read()

HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str):
    requirements = []
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "Text Summarizer",
    version = "0.0.1",
    author = "Chhaya",
    author_email = "chhaya3033@example.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt"),
    description = "A small python package for summarizing text.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ChhayaVarshney/TextSummarizer",
    project_urls = {"Bug Packages" : f"https://github.com/ChhayaVarshney/TextSummarizer/issues"}
)