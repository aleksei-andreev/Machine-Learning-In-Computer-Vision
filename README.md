# YOLOv3-nano Demo

This is the demo of a highly compact `You Only Look Once` Convolutional Neural Network for Object Detection

## Download the materials

Clone this branch using git:

```
git clone --branch Week-1.1 https://github.com/aleksei-andreev/Machine-Learning-in-Computer-Vision.git

cd Machine-Learning-in-Computer-Vision
```

## Create a virtual environment

TensorFlow requires Python 3.7-3.10 to be installed

**Linux/macOS:**

To manage different Python versions and virtual environments, you may install `pyenv` using official guide: https://github.com/pyenv/pyenv#installation/

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

To manage different Python versions and virtual environments, you may install `conda` using official guide: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html

```
    conda create -n venv python=3.8.9
	
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
