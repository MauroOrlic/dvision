#!/bin/sh

#sudo pacman -S clang llvm openshadinglanguage ffmpeg
#mkdir ~/blender-git
cd ~/blender-git
#git clone http://git.blender.org/blender.git
cd blender
git submodule update --init --recursive
git submodule foreach git checkout master
git submodule foreach git pull --rebase origin master

cd ~/blender-git
./blender/build_files/build_environment/install_deps.sh --skip-llvm


mkdir ~/blender-git/linux_build_bpy
cd ~/blender-git/linux_build_bpy
rm -rf *
PYTHON_VERSION="3.8"
CPU_COUNT=16
VENV_NAME="dvision"
VENV_SITE_PACKAGES="$HOME/.virtualenvs/$VENV_NAME/lib/python$PYTHON_VERSION/site-packages"

export PYTHONPATH="/usr/lib/python$PYTHON_VERSION"
export PYTHON_SITE_PACKAGES=$VENV_SITE_PACKAGES
cmake -G "Unix Makefiles" -DWITH_PYTHON_INSTALL=OFF -DWITH_PLAYER=OFF -DWITH_PYTHON_MODULE=ON -DPYTHON_EXECUTABLE="/usr/bin/python$PYTHON_VERSION" -DPYTHON_INCLUDE_CONFIG_DIR="/usr/include/python$PYTHON_VERSION" -DPYTHON_INCLUDE_DIR="/usr/include/python$PYTHON_VERSION" -DPYTHON_LIBRARY="/usr/lib/libpython$PYTHON_VERSION.so" -DPYTHON_SITE_PACKAGES=$VENV_SITE_PACKAGES -DPYTHON_VERSION=$PYTHON_VERSION -DWITH_INSTALL_PORTABLE=ON -DCMAKE_INSTALL_PREFIX=$VENV_SITE_PACKAGES -DWITH_MEM_JEMALLOC=OFF ../blender
make -j $CPU_COUNT install
