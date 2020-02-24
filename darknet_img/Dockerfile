FROM archlinux:latest
RUN pacman -Syyu --noconfirm
RUN pacman -S --noconfirm --needed base-devel git cmake 

# Creating user that will install AUR packages
ARG AUR_USER=aur_user
RUN useradd -m $AUR_USER \
&&  echo "${AUR_USER}:" | chpasswd -e \
&&  echo "$AUR_USER ALL = NOPASSWD: ALL" >> /etc/sudoers

# Installing trizen - AUR package manager
RUN pacman -S --noconfirm --needed pacutils perl-libwww perl-term-ui perl-json perl-data-dump perl-lwp-protocol-https perl-term-readline-gnu \
&&  su $AUR_USER -c 'cd; git clone https://aur.archlinux.org/trizen.git' \
&&  su $AUR_USER -c 'cd; cd trizen; makepkg' \
&&  cd /home/$AUR_USER/trizen \
&&  pacman -U --noconfirm --needed trizen*.pkg.tar* \
&&  cd \
&&  rm -rf /home/$AUR_USER/trizen \
&&  su $AUR_USER -c 'trizen -Syyu --noconfirm'

# Improving package build speed (thread count, disabling package compression)
RUN sed -i 's,#MAKEFLAGS="-j2",MAKEFLAGS="-j$(nproc)",g' /etc/makepkg.conf \
&&  sed -i "s,PKGEXT='.pkg.tar.xz',PKGEXT='.pkg.tar',g" /etc/makepkg.conf

# Installing dependencies
RUN pacman -S --noconfirm --needed cuda cudnn qt5-base opencv
RUN pacman -Rsn --noconfirm opencv
RUN su $AUR_USER -c 'trizen -S --noconfirm --needed opencv3 opencv3-opt'
ENV PATH="/opt/cuda/bin:$PATH"

# Installing Darknet
RUN git clone https://github.com/AlexeyAB/darknet.git \
&&  cd darknet \
&&  mkdir build-release \
&&  cd build-release \
&&  cmake .. \
&&  make \
&&  make install

RUN /darknet/build-release/darknet detector test
