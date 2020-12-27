FROM continuumio/miniconda3:4.8.2

RUN apt-get update
RUN apt install -y build-essential
RUN apt-get install -y libgsl-dev libglu1

ADD environment.yml /tmp/environment.yml
RUN conda update --all
RUN conda env create -f /tmp/environment.yml

# Pull the environment name out of the environment.yml
RUN echo "conda activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" >> ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

ENV CONDA_DEFAULT_ENV $(head -1 /tmp/environment.yml | cut -d' ' -f2)
