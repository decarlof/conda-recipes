#!/bin/bash

mkdir -vp ${PREFIX}/bin;
pwd;

ARCH="$(uname 2>/dev/null)"

export CFLAGS="-m64 -pipe -O2 -march=x86-64 -fPIC"
export CXXFLAGS="${CFLAGS}"
#export CPPFLAGS="-I${PREFIX}/include"
#export LDFLAGS="-L${PREFIX}/lib"

LinuxInstallation() {
    cd hdf4/hdf-4.2.9/;
    chmod +x configure;
    pwd;
    pwd;
    pwd;
    pwd;
    pwd;
    ./configure \
        --disable-static \
        --enable-linux-lfs \
        --with-ssl \
        --with-zlib \
        --prefix=${PREFIX} || return 1;
    make || return 1;
    make install || return 1;

    rm -rf ${PREFIX}/share/hdf4_examples;

    return 0;
}

case ${ARCH} in
    'Linux')
        LinuxInstallation || exit 1;
        ;;
    *)
        echo -e "Unsupported machine type: ${ARCH}";
        exit 1;
        ;;
esac

#POST_LINK="${PREFIX}/bin/.hdf4-post-link.sh"
#cp -v ${RECIPE_DIR}/post-link.sh ${POST_LINK};
#chmod -v 0755 ${POST_LINK};
