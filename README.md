# YOLOv3-nano Demo

This is the demo of a highly compact `You Only Look Once` Convolutional Neural Network for Object Detection

## Download the materials

You may download all the materials needed by either downloading the ZIP file or by cloning the git repository

**ZIP file:**

To download the ZIP file click `Code` -> `Download ZIP` in your browser being on the branch page, then unpack it to the desired location on your hard drive

**git:**

In case `git` is not yet installed on your operating system you may install it using the official guide: https://github.com/git-guides/install-git

Clone this branch using git:

```
git clone --branch Week-1.1 https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision.git
```

After getting all the materials needed change the current working directory by:

```
cd Machine-Learning-in-Computer-Vision
```

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

```
    conda create -n venv python=3.8.8
	
    conda activate venv
```

## Install the dependencies

```
    pip install -r requirements.txt
```

## Run the script

**Linux/macOS:**

```
    python3 demo.py
```

**Windows:**

```
    python demo.py
```
