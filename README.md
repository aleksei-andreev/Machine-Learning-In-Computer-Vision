# YOLOv3-nano Demo

This is the demo of a highly compact `You Only Look Once` Convolutional Neural Network for Object Detection

## Week 1

Branch "Week-1.1" reproduces the first assignment of "Week 1": https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision/tree/Week-1.1

This branch reproduces the second assignment of "Week 1"

## Create a virtual environment

TensorFlow requires Python 3.7-3.10 to be installed

**Linux/macOS:**

To manage different Python versions and virtual environments you may install `pyenv` using the official guide: https://github.com/pyenv/pyenv#installation/

Install Python 3.8.9:

```
    pyenv install 3.8.9
```

Create and activate virtual environment:

```
    pyenv virtualenv 3.8.9 venv

    pyenv activate venv
```

**Windows:**

To manage different Python versions and virtual environments, you may install `conda` using the official guide: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html

Then create and activate virtual environment:

```
    conda create -n venv python=3.8.8

    conda activate venv
```

## Install the package from a local copy of the repository

### Download the materials

You may download all the materials needed by either downloading the ZIP file or by cloning the git repository

**ZIP file:**

To download the ZIP file click `Code` -> `Download ZIP` in your browser being on the branch page, then unpack it to the desired location on your hard drive

**git:**

In case `git` is not yet installed on your operating system you may install it using the official guide: https://github.com/git-guides/install-git

Clone this branch using git:

```
git clone --branch Week-1.2 https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision.git
```

After getting all the materials needed change the current working directory:

```
cd Machine-Learning-in-Computer-Vision
```

### Build the package

The package is already built, but it is possible to build it yourself. To do so you must have the `build` package installed. If you don't have it, you may install it:

```
    pip install build
```

Then build the package:

**Linux/macOS:**

```
    python3 -m build
```

**Windows:**

```
    python -m build
```

Finally, install the main package:

```
    pip install dist/MachineLearninginComputerVision-0.1.0.tar.gz
```

## Install the package directly from the repository

Use the following code to install the package directly from the repository without downloading all the materials:

```
    pip install git+https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision.git@Week-1.2
```

## Run the script

To run the script just use the command below:

```
    demo
```
