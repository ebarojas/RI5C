#!/usr/bin/env bash
 # Script for install python 3.6

if command -v python3.6 &>/dev/null; then
    echo "=> Python 3.6.8 is installed"
else
    echo "=> Begin installing python3.6.8..."
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev
    # get source code
    cd $HOME
    wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
    tar -zxvf Python-3.6.8.tgz
    cd Python-3.6.8
    # build & install
    echo "=> build & install..."
    # --enable-optimizations seems to enable some features like profile-guided
    # optimization. It increases build times but seems to result in a faster interpreter
    # by 10% or so according to some benchmarks.
    ./configure --enable-optimizations
    make
    sudo make altinstall  # is used to prevent replacing the default python binary file
    # cleanup
    cd ..
    sudo rm -fr ./Python-3.6.8*
    # upgrade (just in case)
    sudo python3.6 -m pip install -U pip
    sudo python3.6 -m pip install -U setuptools
    echo "=> End installing python3.6.8..."
 fi