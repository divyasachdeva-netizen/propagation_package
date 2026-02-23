FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install dependencies
RUN apt-get update && apt-get install -y \
    git g++ gcc cmake make swig \
    python3 python3-pip python3-dev python3-distutils python3-venv \
    libgsl-dev libboost-all-dev libfftw3-dev libhdf5-dev libeigen3-dev \
    && apt-get clean

# Build CRPropa
RUN git clone https://github.com/CRPropa/CRPropa3.git /opt/CRPropa3 \
    && mkdir /opt/CRPropa3/build \
    && cd /opt/CRPropa3/build \
    && cmake .. -DPYTHON_BINDINGS=ON \
    && make -j2 \
    && make install

# Python packages
RUN pip install jupyterlab numpy scipy matplotlib h5py

ENV PYTHONPATH="/usr/local/lib/python3.10/dist-packages:${PYTHONPATH}"
