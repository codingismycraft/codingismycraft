################################################################################
#
# Substitutes the default user and group in the Ubuntu image with a new user.
#
# docker build --build-arg USERNAME=<user-name> -t <image-name> .
#
################################################################################

FROM ubuntu:latest

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

# Remove the existing user and group if they exist
RUN if id "ubuntu" 2>/dev/null; then userdel -r ubuntu; fi && \
    if getent group "${USER_GID}"; then groupdel $(getent group "${USER_GID}" | cut -d: -f1); fi

# Create new group and user with UID and GID "${USER_GID}"
RUN groupadd -g "${USER_GID}" "$USERNAME"  && \
    useradd -u "${USER_UID}" -g "${USER_GID}" -m -s /bin/bash "$USERNAME"


# Install all necessary dependencies as root
RUN apt-get update && apt-get install -y \
    git build-essential libncurses5-dev libgtk2.0-dev libatk1.0-dev libcairo2-dev \
    python3-dev python3-pip libx11-dev libxpm-dev libxt-dev libsm-dev libperl-dev \
    liblua5.2-dev ruby-dev lua5.2 curl ca-certificates wget fzf golang sudo adduser \
    && rm -rf /var/lib/apt/lists/*  # Clean up apt cache to reduce image size

# Clone Vim source, configure with various language and GUI support, build and
# install as root, then clean up
RUN git clone https://github.com/vim/vim.git /usr/local/src/vim \
    && cd /usr/local/src/vim \
    && ./configure --with-features=huge --enable-multibyte --enable-rubyinterp=yes \
       --enable-python3interp=yes --with-python3-config-dir=$(python3-config --configdir) \
       --enable-perlinterp=yes --enable-luainterp=yes --enable-gui=gtk3 --enable-cscope \
       --prefix=/usr/local --enable-clipboard \
    && make -j$(nproc) \
    && make install \
    && cd / \
    && rm -rf /usr/local/src/vim  # Remove source code to keep image clean

# Check that build arguments for user, UID, and GID are not empty
RUN test -n "$USERNAME" && test -n "$USER_UID" && test -n "$USER_GID" \
    || (echo "Missing build args: USERNAME=$USERNAME, USER_UID=$USER_UID, USER_GID=$USER_GID" && exit 1)

# Create group with specified GID if it doesn't exist
RUN if ! getent group "${USER_GID}" >/dev/null; then \
      addgroup --gid "${USER_GID}" "${USERNAME}"; \
    fi

# Create user with specified UID and GID if it doesn't exist
RUN if ! id -u "${USER_UID}" >/dev/null 2>&1; then \
      adduser --uid "${USER_UID}" --gid "${USER_GID}" --disabled-password --gecos "" "${USERNAME}"; \
    fi

# Allow the user to run sudo commands without a password
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Ensure the user owns their home directory (ignore errors if directory does
# not exist)
RUN chown -R ${USER_UID}:${USER_GID} /home/${USERNAME} || true

# Switch to the non-root user
USER ${USERNAME}

# Set working directory and HOME for the new user (hard-coded or using build arg with default)
WORKDIR /home/${USERNAME}

#ENV HOME=/home/${USERNAME}
#ENV NVM_DIR=$HOME/.nvm

# Install NVM and Node.js as the user, with $HOME set correctly
#RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && \
#    . "$NVM_DIR/nvm.sh" && \
#    nvm install 22

# Optionally add Node.js to PATH for subsequent Docker RUN commands and containers
# ENV PATH=$NVM_DIR/versions/node/v22.*/bin:$PATH
