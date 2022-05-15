# Setting up a local Python environment

All the exercises, demos and labs are coded in Python and they are run using Jupyter notebooks. This tutorial describes the necessary steps needed to setup a Python environment in your computer.

## Installing Anaconda
Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. We will use it to manage our Python installation and the necessary packages and libraries. 

If you do not have Anaconda installed in your computer, please visit this [this page](https://www.anaconda.com/products/distribution#Downloads) to download the version that suits your OS and install it. 

Once you have installed Anaconda, you will notice that it offers a GUI for execution. This tutorial assumes you will work from the command line. Nevertheless, all the described steps can be also performed using the GUI.

## Creating a virtual environment
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system. This allows the use different versions of the same package for different projects. Therefore, it is highly recommended to create a new virtual environment for every project or course.

If you are working on a Mac or Linux machine, you will need to open a terminal to create a new virtual environment. If you are working on a Windows machine, you will need to open an Anaconda prompt terminal. It can be found in the start menu.

Once the terminal is open, you will need to execute the following commands to create the MALIS virtual environment:

**Add conda-forge as a channel**
By default, the conda package manager installs packages from the defaults channel. Apart from the official defaults channel, there are some third-party channels available for hosting and managing packages. One such channel is conda-forge. Conda-forge is community-led channel that provides latest conda packages for a wide-range of software.  Given its utility, we will add it to our configuration. As such, the conda package manager will consider it in top priority when installing new packages.

```bash
conda config --add channels conda-forge
```

**Create the MALIS virtual environment**
```bash
conda create --name malis python=3.8
```

**Activate the MALIS virtual envirnment**
```bash
conda activate malis
```

The latter command activates the malis virtual environment. Note that every time you open a terminal, by default, you will be in the base environment. You will have to use `conda activate malis` every time you want to work in it. Once you are done with your work, you can deactivate it using

**Deactivate a virtual envirnment**
```bash
conda deactivate
```

## Installing the necessary libraries and packages
Aside Python, during the course we will be using several packages that need to be installed in your newly created virtual environment. A brief description is provided in the following:

* Numpy: Library for matrix and array manipulation and, more generally, numerical operations
* Scipy: Library for scientific computing
* Pandas:  Offers data structures and operations for manipulating numerical tables and time series
* Matplotlib, Seaborn, Plotly, ipywidgets: These are different libraries for plotting and data visualization
* scikit-learn: Library offering a wide set of Machine learning algorithms
* tqdm: Progress bar

Some of these libraries already come installed in the base conda environment. However, when a new virtual environment is created, it is empty requiring to install all the necessary packages. 

Aside the listed libraries, we will also need to install Jupyter notebooks and Jupyter Lab. To install the new packages, first make sure that you have activated the malis environment. Then, execute the following:

**Install the necessary packages**
```bash
conda install jupyter jupyterlab numpy scipy pandas matplotlib seaborn plotly jupyter-dash scikit-learn ipywidgets tqdm 
```

## Other important commands

**Deactivate an active virtual environment**
```bash
conda deactivate
```

**List virtual environments**
```bash
conda env list
```

**Remove a virtual environment**
```bash
conda env remove -n <name-of-virtual-environment>
```