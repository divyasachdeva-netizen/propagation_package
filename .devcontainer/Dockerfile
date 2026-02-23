FROM ubuntu:22.04

# -----------------------------
# Basic system + Python packages
# -----------------------------
RUN apt-get update && \
    apt-get install -y \
    git wget curl \
    build-essential cmake pkg-config \
    python3 python3-pip python3-dev python3-setuptools \
    libgsl-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install CRPropa from source
# -----------------------------
RUN git clone --depth 1 https://github.com/CRPropa/CRPropa3.git /opt/CRPropa3 && \
    cd /opt/CRPropa3 && \
    mkdir build && cd build && \
    cmake .. -DCRPROPA_BUILD_PYTHON_MODULE=ON -DPython_EXECUTABLE=/usr/bin/python3 && \
    make -j4 && make install

# Ensure Python can find CRPropa
ENV PYTHONPATH="/usr/local/lib/python3.10/dist-packages:${PYTHONPATH}"

# Test CRPropa install
RUN python3 - <<EOF
import crpropa
print("CRPropa installed OK:", crpropa.__version__)
EOF

# -----------------------------
# Default settings
# -----------------------------
CMD ["/bin/bash"]
