FROM crpropa/crpropa:3.2.0

# Install Python + Jupyter + plotting tools
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install jupyterlab matplotlib numpy scipy h5py astropy

CMD ["/bin/bash"]
