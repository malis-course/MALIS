# Using Git and Git repositories

All the exercises, demos and labs will be on GitHub and GitLab. These are websites that host Git repositories. This tutorial shows you how to set-up Git in your local machine and how to use an online repository, such as GitHub or GitLab.

## Definitions
**Git** is a free and open source distributed version control system designed for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development.

**Version control system** is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. In short a version control system tracks and provides control over changes to source code.

**Software repository** or simply repository or repo, is a storage location for software packages. A software repository is typically managed by source version control or repository systems.

**GitHub and GitLab** are two online websites hosting Git repositories.

## Learning to use Git
A detailed introduction to Git can be found in the [Git online documentation](https://docs.github.com/en/get-started/using-git/about-git). A faster alternative is to keep at hand the [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf).

To run the exercises and demos, and to work with the labs you will only need to master three git commands `clone`, `fetch` and `pull`. However, you may be interested in digging deeper into it if you want to maintain a repository for your MALIS project.

### Git documentation and resources
* [Git online documentation](https://docs.github.com/en/get-started/using-git/about-git)
* [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## Creating an account
By being enrolled at EURECOM, you automatically have a GitLab account. Go to https://gitlab.eurecom.fr/ and use your Unix credentials to login.

If you wish to create a GitHub account, follow this [link](https://github.com/signup?source=login) to create one.

## Installing Git in your computer
If you are unsure about already having installed Git in your computer, open a terminal and type git. If you have it, you will see some text displayed documenting its usage. Otherwise, you will see an error indicating that the command has not been recognized by the system.

To install Git, you may follow any of the links below:
* For Window users - https://gitforwindows.org/
* For Mac users - Typically, Apple packs a binary version of Git with Xcode. If you do not have Xcode, please refer to https://git-scm.com/download/mac for a fresh Git install
* For Linux users - Usually, Linux distributions come with Git already installed. If you wish to update your version, please refer to https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Using a GUI to work with Git
This tutorial assumes you will be working from the command line. If you prefer to work with a graphical user interface (GUI), you can download and install [GitHub Desktop](https://desktop.github.com/). Note that GitHub Desktop has been conceived with GitHub. You may try to configure it to work with GitLab by following the instructions from [this website](https://itnext.io/how-to-use-github-desktop-with-gitlab-cd4d2de3d104).

## Cloning the MALIS course repository
The course material can be found from two sources. It is publicly hosted in GitHub [link](https://github.com/malis-course/MALIS) and it can also be found in EURECOM's priavte GitLab repository [link](https://gitlab.eurecom.fr/zuluaga/MALIS).

To get a copy of the repository, you need to clone it. The `git clone` operation allow to create a copy of an existing repository. To do this, open a git terminal and navigate to the folder where you want to store the local copy of your repository. Then, type the following in the command line:

*Cloning from GitLab*
```bash
git clone https://gitlab.eurecom.fr/zuluaga/MALIS.git .
```

*Cloning from GitHub*
```bash
git clone https://github.com/malis-course/MALIS.git .
```

If the operation is succesful, you should be able to see a newly created folder, named MALIS, in the directory where you currently stand.

If you are using a visual GUI, such as GitHub Desktop, you can find a a step-by-step tutorial [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).

## Using Git in MALIS
The exercises, demos and labs are maintained in the course's repository. To update your local copy of the repository, you need to `pull` the changes from the remote repository.

To do so with GitHub Desktop, you will first need to Fetch origin, and then Pull origin. We recommend fetching and pulling anytime you want to work on the exercises, in order to ensure that your local copy is up-to-date:

```bash
git fetch origin
git pull
```
For the exercises, demos and labs there is no need to add, commit and push your changes anywhere. You may be interested in maintaining your own repository to keep track of the changes of your MALIS project. In that case, you will need these operations.
