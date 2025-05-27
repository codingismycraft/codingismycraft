##############################################################################
#
# Dockerfile for a basic CUDA environment with Python and NumPy
# Use the official NVIDIA CUDA base image for Ubuntu 22.04
# Before building this Dockerfile, ensure you have Docker installed and the
# NVIDIA Container Toolkit set up.
#
# To build and run this Dockerfile, use the following commands:
#
# docker run --rm -it --runtime=nvidia --gpus all my-cuda-app bash
#
# See here also:
#
# https://www.gpu-mart.com/blog/install-nvidia-container-toolkit
# for more details.
##############################################################################


FROM nvidia/cuda:12.4.0-base-ubuntu22.04


# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Install Python packages
RUN pip3 install --upgrade pip
RUN pip3 install numpy scipy

# Set up your application here
# COPY ./your-app /app

# Set the command to run when the container starts
CMD ["nvidia-smi"]
