# Dockerized Development Environment with Vim Integration

This directory contains sample files for setting up a Docker container tailored
for development, providing a consistent Vim experience between your host and
the container.

## Overview

The provided `Dockerfile` and `docker-compose.yml` allow you to:

- **Map your Vim configuration and plugins**: Your `.vim`, `.vimrc`, and
  `.bashrc` from the host are mapped directly into the container, ensuring that
  your personalized Vim setup (including plugins) is available inside Docker.

- **Share clipboard with the host**: Clipboard functionality is shared,
  enabling seamless copy-paste operations between the host and the container.

- **Maintain user consistency**: The container user matches your host user. By
  default, both the user ID (UID) and group ID (GID) are set to `1000` to align
  with typical Linux user defaults. This ensures that mapped files and
  directories have the correct permissions and function as expected.

## Usage

These files serve as a template for creating custom development containers. For
example, you can extend this setup to include additional tools or libraries,
such as NVIDIA CUDA for C/C++ development or other specialized environments.

## Customization

- Adjust the `Dockerfile` and `docker-compose.yml` as needed to install other
  packages or change user/group settings.

- Feel free to use this as a starting point for more complex development
  environments.

## Notes

- Vim is installed from the source code inside the container.

- The setup aims to provide a development environment inside Docker that
  closely mirrors your host experience, especially for Vim users.

