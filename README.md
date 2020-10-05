# popsimenv

This is a private testing repository for creating testing environments - for running population genetics simulations using the stdpopsim open-source library.
The original testing repository popsim-consortium/analysis is copied and modified to our objectives.
For further reading see:
https://github.com/popsim-consortium/analysis
https://github.com/popsim-consortium/stdpopsim

# installations:

> You need to install Docker before going any further.

The Dockerfile takes care to all the installations and dependencies required. just follow the 'usage' section below.
NOTE: please ignore the installation instructions detailed in the README.md files under the 'analysis'.

# usage:

1. (One time only) Inside this directory, run the following bash command to build the image docker using the Dockerfile:
    ```bash
    docker build -t popsimenv-image .
    ```

2. Inside this directory, run the container interactively with the src folder as shared volume:
for Mac/Linux users:
    ```bash
    docker run -t -i -v $(pwd)/src:/code/src popsimenv-image //bin/bash
    ```
for Windows users:
    ```bash
    docker run -t -i -v %cd%/src:/code/src popsimenv-image //bin/bash
    ```
   
3. Activate the conda enviroment:
    ```bash
    conda activate popsim_env_test
    ```

> Using the -v option enables syncing the src folder between the host and the container for easier editing.
