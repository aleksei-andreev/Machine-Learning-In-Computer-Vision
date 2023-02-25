import io
import os.path as osp
import re

from setuptools import find_packages, setup


def get_version():
    current_dir = osp.abspath(osp.dirname(__file__))
    version_file = osp.join(current_dir, "src", "MachineLearninginComputerVision", "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        text = f.read()
    return re.search(r"^__version__ = [\"']([^\"']*)[\"']", text, re.M).group(1)


def get_long_description():
    current_dir = osp.abspath(osp.dirname(__file__))
    long_description_file = osp.join(current_dir, "README.md")
    with open(long_description_file, encoding="utf-8") as f:
        long_description = f.read()
    return long_description


def get_dependencies():
    current_dir = osp.abspath(osp.dirname(__file__))
    requirements_file = osp.join(current_dir, "requirements.txt")
    with open(requirements_file, encoding="utf-8") as f:
        dependencies = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]
    return dependencies


setup(
    name="MachineLearninginComputerVision",
    version=get_version(),
    author="Aleksei Andreev",
    author_email="aaandreev_6@edu.hse.ru",
    description="YOLOv3_nano Demo",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=get_dependencies(),
    python_requires=">=3.7,<3.10",
    package_data={"MachineLearninginComputerVision": ["core/*", "data/classes/*", "model/*", "sample/*"]},
    entry_points={"console_scripts": ["demo=MachineLearninginComputerVision.demo:main"]},
)
