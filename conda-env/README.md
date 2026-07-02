# Conda

[Conda](https://docs.conda.io) is an open-source package management system and environment management system.
We will use Conda to help us create and manage a Python environment with the specific packages we'll use in this course.

## Installation

We will use a minimal installer for Conda called [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
Follow the instructions below for your operating system.
Note that in all cases, we will be using Python 3.x, _not_ Python 2.7, so make sure you are downloading and installing the correct version of Conda/Miniconda.

### Windows

This section assumes you are installing Conda using a Windows installer for use with the traditional Windows command prompt.
If you are using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl) (WSL), use the Linux instructions instead.

1.  Download the [latest version](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) of Miniconda from the [Windows installer section](https://docs.conda.io/en/latest/miniconda.html#windows-installers) of the Miniconda website

2.  [Install Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), and configure it with the following options if prompted:

    - Yes, add to path

    - No, do not make the system's default Python

    - Yes, create Start menu entries

3.  Verify that your install works as expected using the testing steps described in the [Miniconda installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)

### macOS

Follow the [macOS installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html) on the Conda website.
Note: take care to install the correct version for your [Mac's CPU architecture](https://support.apple.com/en-us/HT211814).

Alternatively, you can instead use [Homebrew](https://brew.sh) to install Miniconda using the [`miniconda` cask](https://formulae.brew.sh/cask/miniconda).

### Linux

Some distributions package Miniconda; try searching for `conda` or `miniconda` with your system package manager (e.g., `apt`, `dnf`).
For example, on recent versions of Fedora, you can run `dnf install conda` to install Conda.
Note that these packaged versions may be somewhat out of date, however, that is usually not an issue in day-to-day use unless you are reliant on bleeding-edge features of the `conda` executable itself.

If not available in your system package manager out of the box, you can also add [repositories for RPM- and Debian-based distributions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/rpm-debian.html), and then install Conda using your system package manager.

In all other cases, follow the [Linux installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html) on the Conda website.

## Environment Setup

Once you have Conda installed, you will need to set up a Conda environment that contains Python itself and all of the supporting packages we'll be using in the course.
This is a one-time operation; once the environment is created, you'll simply activate and use it for various programming assignments and projects throughout the course.

To create your Conda environment, complete the following steps:

1.  Open a new command-line shell

    - On Windows: run the "Anaconda Prompt" application from the Start menu

    - On macOS: run the "Terminal" application (located in your Applications > Utilities folder)

2.  In your shell, change directory to the location where you are storing your coursework for this course

3.  Clone this repository to your local machine:

    ```git clone https://gitlab.com/georgefox/coursework/csis344/starter/conda-env.git```

    (Note: if you are using Windows, you may need to install [Git](https://git-scm.com/downloads) before proceeding.
    You will be prompted to configure many different options during installation; ask for help during class or office hours if needed.)

    (Note: if you are using macOS, you may be prompted to download and install the [Xcode Command Line Tools](https://developer.apple.com/xcode/resources) when you first use the `git` command on the command line.
    You should follow those prompts and complete that process, then try cloning the repository again.)

    If you are using HTTPS rather than SSH, you will need to [create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token), taking care to create it with the `read_repository` and `write_repository` [scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes), and use it rather than your GitLab password when cloning.

4.  Change directory to the newly-cloned `conda-env` directory

5.  Create the `csis344` Conda environment:

    ```conda env create -f ```[`environment.yml`](https://gitlab.com/georgefox/coursework/csis344/starter/conda-env/-/blob/master/environment.yml)

6.  Once the environment is created, activate it:

    ```conda activate csis344```

7.  Test your environment by running the provided test script:

    ```python ```[`test_env.py`](https://gitlab.com/georgefox/coursework/csis344/starter/conda-env/-/blob/master/test_env.py)

If all works as expected, the test script will import several Python packages and report the installed version for each.
If any of the packages report an error, verify that you have first activated the correct Conda environment.
