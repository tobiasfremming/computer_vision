# TDT4195 - Visual Computing Fundamentals

This is the repository for the assignments in TDT4195. Originally written by Håkon Hukkelas. Maintained and updated by Michael Staff Larsen.

## Overview

The assignment grading will be conducted through our INGInious web server at [https://tdt4195.idi.ntnu.no/](https://tdt4195.idi.ntnu.no/). Please note that VPN is nesecary when accessing the site outside the NTNU network. For VPN installation and configuration, see [https://i.ntnu.no/wiki/-/wiki/English/Install+VPN](https://i.ntnu.no/wiki/-/wiki/English/Install+VPN)


The purpous of the starter code is to enable you to test your code before submitting to the grading server.


All assignments are anounced on blackboard, and have the following delivery dates:

1. Assignment 1: Friday October 25th, 23:59 PM
2. Assignment 2 Friday November 8th ,23:59 PM
3. Assignment 3: Friday November 22th, 23:59 PM

The starting source code for each assignment will be published during the semester.


### Assignment 1
This assignment will give you an introduction to basic image processing with python, filtering in the spatial domain, and a simple introduction to building fully-connected neural networks with PyTorch.

### Assignment 2
We will introduce you to classifying images with Convolutional Neural Networks (CNNs) and how we can use the frequency domain for image filtering.

### Assignment 3
We will explore how we can segment an image into foreground and background by using basic segmentation algorithms, such as thresholding and region growing.
Furthermore, you will use binary morphological operations to manipulate the contents of a binary image.


## Preparing yourself for the assignments
In this course, we expect basic knowledge of python programming and git. To refresh your knowledge, we recommend the following resources:

- [CS231N Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/)
- [Introduction to git](https://guides.github.com/introduction/git-handbook/)

### Setting up your environment
In this course, all assignments are given in python. You can do the assignments on the following resources:

- Your own computer: Follow our [python setup instructions](tutorials/python_setup_instructions.md) to setup your own environment
- Cybele computers: The environment is already setup for you, check out our [practical information](working_on_cybele_computers.md) on how to work on these computers

### Download the starter code

Clone this repostiory:

```bash
git clone https://github.com/TDT4195-tutorial/TDT4195-StarterCode-2024.git
```

You can also download this repository as a zip file and unzip it on your computer.


**There might be minor typos or minor alterations to the starter code**. If this happens, we will notify you on blackboard and you can update your starter code by doing (In your assignment directory):

```
git pull origin main
```

**If you wish to commit your changes to your own Git repo**, you can do so by:
1. Creating an empty private repository
2. While inside the starter code directory, run `git remote rename origin upstream`
3. `git remote add origin YOUR_REPO_URL`
4. `git push -u origin main`

Then, when a new change is added to the upstream repo, you can add it to your own repo by running:
1. `git pull upstream main`
2. `git push`

*Note:* it is recommended to use git through a client like VS Code and sign in with your GitHub user. If you use git in a terminal, you may need to authenticate with GitHub with a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) as your password.