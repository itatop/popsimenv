# popsimenv

This is a private testing repository for creating testing environments - for running population genetics simulations using the stdpopsim open-source library.
The original testing repository popsim-consortium/analysis is copied and modified to our objectives.
For further reading see:
https://github.com/popsim-consortium/analysis
https://github.com/popsim-consortium/stdpopsim

# usage:

> You need to install Docker before going any further.

1. (One time only) Inside this directory, run the following bash command to build the image docker using the Dockerfile:
    ```bash
    docker build -t popsimenv-image .
    ```

2. Inside this directory, run the container interactively with the src folder as shared volume:
    ```bash
    docker run -t -i -v $(pwd)/src:/code/src popsimenv-image /bin/bash
    ```
   
> Using the -v option enables syncing the src folder between the host and the container for easier editing.

