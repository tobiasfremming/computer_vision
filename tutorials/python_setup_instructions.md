# Python Setup Instructions (Local)

## Setup

**Installing Miniconda:** We recommend using [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) which provides an easy way for you to handle package dependencies. Please be sure to download the Python 3 version.

**Miniconda Virtual environment:** Once you have Miniconda installed, it makes sense to create a virtual environment for the course. If you choose not to use a virtual environment, it is up to you to make sure that all dependencies for the code are installed globally on your machine. To set up a virtual environment, run (in a terminal) 

```bash
conda conda env create --file environment.yml
```

to create a environment called `tdt4195`, where all the dependencies are described in environment.yml

Then, to activate and enter the environment, run

```bash
conda activate tdt4195
```

To exit, you can simply close the window, or run

```bash
conda deactivate tdt4195
```

Note that every time you want to work on the assignment, you should run `conda activate tdt4195` (change to the name of your virtual env).

You may refer to [this page](https://conda.io/docs/user-guide/tasks/manage-environments.html) for more detailed instructions on managing virtual environments with Anaconda.

## Installing additional packages
Use pip to install additional packages as needed

```bash
pip install some_package
```

**Note**, By default, pytorch is installed with cpu only version. If you have a PC with NVIDIA GPU (windows) then you need to install pytorch and torchvision with cuda support. To do that, follow tutorial on the pytorch website https://pytorch.org/get-started/locally/. GPU support should be installed by default for linux if applicable.



## Launching jupyter notebook

Once you have finished the environment setup, and installed the required packages, you can launch jupyter notebook with the command:

```bash
jupyter notebook
```

Then, if you open a jupyter notebook file (`.ipynb`), you will see the active environment in the top right corner. To change the kernel to the right environment select `kernel` -> `change kernel` -> `Python tdt4195`. 

If your environment is not showing up in the list of kernels, you can take a quick look on [this stackoverflow post](https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook).