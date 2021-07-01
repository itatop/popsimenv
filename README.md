# popsimenv

This is a private testing repository for creating a testing environment for running population genetics simulations using the stdpopsim open-source library.
The original testing repository popsim-consortium/analysis is copied and modified to our objectives.
For further reading see:

https://github.com/popsim-consortium/analysis
https://github.com/popsim-consortium/stdpopsim

# work through:

> src folder

# modification of the image:

> done by changing Dockerfile and environment.yml

# installations:

> You need to install Git and Docker before going any further:

https://git-scm.com/downloads

https://www.docker.com/products/docker-desktop

The Dockerfile takes care of all the installations and dependencies required. just follow the 'usage' section below.

# usage:

first time only:

1. Clone the popsimenv directory from git (current page if you are reading these lines from the popsimenv repository)

2. Inside popsimenv directory, run the following command to build the image docker using the Dockerfile:
    ```bash
    docker build -t popsimenv-image .
    ```

Opening a working session:

1. Open Docker Desktop app.

2. Inside popsimenv directory, run the container interactively with the src folder as shared volume:

* for Mac/Linux users:
    ```bash
    docker run --rm -t -i --name popsimenv --mount type=bind,source=$(pwd)/src,target=/code/src popsimenv-image /bin/bash

    ```

* for Windows users:
    ```bash
    docker run --rm -t -i --name popsimenv --mount type=bind,source=%cd%/src,target=/code/src popsimenv-image //bin/bash
    ```

3. Activate the conda environment:
    ```bash
    conda activate popsim_env_test
    ```
4. The shared volume of the image and your file system is (through image):
    ```bash
    /code/src
    ```

Running Snakefile:
1. for example: (run from a directory of an experiment, as in the template directory)
    ```bash
    snakemake -j 1 --config config="experiment"
    ```

