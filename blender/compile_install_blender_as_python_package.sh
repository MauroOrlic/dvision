#!/bin/sh

mkdir ~/blender-git
cd ~/blender-git || exit
#git clone http://git.blender.org/blender.git
cd blender || exit
git submodule update --init --recursive
git submodule foreach git checkout master
git submodule foreach git pull --rebase origin master

cd ~/blender-git || exit
sudo pacman -S clang llvm openshadinglanguage ffmpeg --noconfirm --needed
pip install numpy
./blender/build_files/build_environment/install_deps.sh --skip-llvm

mkdir ~/blender-git/linux_build_bpy
cd ~/blender-git/linux_build_bpy || exit
rm -rf  -- *
PYTHON_VERSION=$(python -c "import sys; print(str(sys.version_info[0]) + '.' + str(sys.version_info[1]))")
echo "Found python version: $PYTHON_VERSION"
SITE_PACKAGES=$(python -c "import sys; print([path for path in sys.path if 'site-packages' in path][0])")
echo "Found python site packages: $SITE_PACKAGES"

export PYTHONPATH="/usr/lib/python$PYTHON_VERSION"
export PYTHON_SITE_PACKAGES=$SITE_PACKAGES
cmake -G "Unix Makefiles" -DWITH_PYTHON_INSTALL=OFF -DWITH_PLAYER=OFF -DWITH_PYTHON_MODULE=ON -DPYTHON_EXECUTABLE="/usr/bin/python$PYTHON_VERSION" -DPYTHON_INCLUDE_CONFIG_DIR="/usr/include/python$PYTHON_VERSION" -DPYTHON_INCLUDE_DIR="/usr/include/python$PYTHON_VERSION" -DPYTHON_LIBRARY="/usr/lib/libpython$PYTHON_VERSION.so" -DPYTHON_SITE_PACKAGES=$SITE_PACKAGES -DPYTHON_VERSION=$PYTHON_VERSION -DWITH_INSTALL_PORTABLE=ON -DCMAKE_INSTALL_PREFIX=$SITE_PACKAGES -DWITH_MEM_JEMALLOC=OFF ../blender
make -j "$(nproc)" install
