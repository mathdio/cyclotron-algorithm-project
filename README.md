# ⚛️ Cycloton Algorithm
An nlgorith project to practice data sctructure and algorithm efficiency.

## 💻 About this project
The algorithm in this project has a function called `cyclotron` that circulate a particle inside a cyclotron. The cycles for each particle type is unique. The first parameter of cyclotron function is the matrix value, and the second one is the particle type.

## 🛠️ Built with
<a href="https://docs.python.org/3/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>

## 🎯 Used skills
- Good practices in data structure, functions, and algorithm efficiency

## 🏁 Getting started
### 🐍 Installing Python 3
You will need Python 3 in order to run the application. You can see how to install it [here](https://wiki.python.org/moin/BeginnersGuide/Download).
Once Python 3 is installed, you can follow the next steps to create a virtual enviroment and install the dependencies in it.

### 🌱 Creating virtual enviroment and installing dependencies
To create the virtual enviroment, run:
```
python3 -m venv .venv
```
To activate the virtual enviroment in a shell enviroment, run:
```
source .venv/bin/activate
```
To deactivate the virtual enviroment, you can simply run the command `deactivate`.

To install the dependencies in virtual enviroment, run:
```
python3 -m pip install -r dev-requirements.txt
```

## 🧪 Testing
To execute all tests, in virtual enviroment run:
```
python3 -m pytest
```
If some issue occurs, you can alternatively run `python3 -m pytest -s -vv`.

To execute one specifict test file, you can run the command with the file path. Example:
```
python3 -m pytest tests/file_path/file_name.py
```
To execute one specific test function, you can run the command with the flag `-k` and the function. Example:
```
python3 -m pytest -k function_name
```
