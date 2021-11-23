# How to run pain.py

Here we will run pain.py script with using virtual environment. Credits (https://github.com/krglkvrmn/Virtual_environment_research)

# Downloading

Download the code from the github link.

`cd Virtual_environment_research-master`

# OS and Python versions

MacOS 11.0.1
Python 3.9.7

# Creating conda environment and installing dependencies

`conda create --name py39 python=3.9`
`conda activate py39`

`pip3 install <module>`

## Hints and additional requirements:

You can install scanpy dependencies via conda

`conda install seaborn scikit-learn statsmodels numba pytables`

`conda install -c conda-forge python-igraph leidenalg`

After that you can run the `pip3 install command` on the requirements list from this repository branch

# Finish your work

Do not forget to deactivate conda environment after usage. Be careful and check if you are not already in the base environment, in this case the whole conda environment will be deactivated.
`conda deactivate`

