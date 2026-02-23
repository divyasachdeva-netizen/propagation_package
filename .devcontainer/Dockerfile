FROM mambaorg/micromamba:1.5.2

USER root

RUN apt-get update && \
    apt-get install -y build-essential cmake git wget python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Create environment and install CRPropa
RUN micromamba create -y -n crp -c conda-forge crpropa python=3.10 \
    && micromamba clean --all --yes

ENV MAMBA_DEFAULT_ENV=crp
ENV PATH=/opt/conda/envs/crp/bin:$PATH

RUN python3 -c "import crpropa; print('CRPropa OK:', crpropa.__version__)"
