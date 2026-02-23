FROM ubuntu:22.04

# Install Python 3.10
RUN apt update && apt install -y \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update && apt install -y \
    python3.10 python3.10-dev python3.10-distutils python3.10-venv \
    git g++ gcc cmake make swig \
    libgsl-dev libboost-all-dev libfftw3-dev libhdf5-dev libeigen3-dev \
    wget curl vim

# Make python3.10 the default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Install pip for python3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# Build CRPropa
RUN git clone https://github.com/CRPropa/CRPropa3.git /opt/CRPropa3 && \
    mkdir /opt/CRPropa3/build && cd /opt/CRPropa3/build && \
    cmake .. -DPYTHON_EXECUTABLE=/usr/bin/python3.10 -DPYTHON_BINDINGS=ON && \
    make -j4 && make install

# Install Python bindings
RUN cp -r /opt/CRPropa3/build/bindings/python/* /usr/local/lib/python3.10/dist-packages/

ENV PYTHONPATH="/usr/local/lib/python3.10/dist-packages:${PYTHONPATH}"

# Install Jupyter + scientific python stack
RUN python3.10 -m pip install jupyterlab numpy scipy matplotlib h5py
