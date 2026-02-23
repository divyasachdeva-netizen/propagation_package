#!/usr/bin/env bash
set -e

sudo apt update

sudo apt install -y \
    git g++ gcc cmake make \
    python3-dev python3-pip python3-setuptools \
    libgsl-dev libboost-all-dev libfftw3-dev libhdf5-dev \
    libeigen3-dev

# Build CRPropa
git clone --depth=1 https://github.com/CRPropa/CRPropa3.git /tmp/CRPropa3
mkdir /tmp/CRPropa3/build
cd /tmp/CRPropa3/build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make -j4
sudo make install

# Install Python bindings
sudo pip install numpy h5py matplotlib
