#!/bin/bash
mkdir -p rmtrash-${RMTRASH_VERS}/rmtrash-${RMTRASH_VERS} && \
    cp configure rmtrash-${RMTRASH_VERS}/ && \
    cp rmtrash rmtrash-${RMTRASH_VERS}/rmtrash-${RMTRASH_VERS}/rmtrash && \
    cp rmdirtrash rmtrash-${RMTRASH_VERS}/rmtrash-${RMTRASH_VERS}/rmdirtrash && \
    tar cvfz rmtrash-${RMTRASH_VERS}.tar.gz rmtrash-${RMTRASH_VERS} && \
    cp rmtrash.spec ~/rpmbuild/SPECS/ && \
    cp rmtrash-${RMTRASH_VERS}.tar.gz ~/rpmbuild/SOURCES/ && \
    rpmbuild -ba ~/rpmbuild/SPECS/rmtrash.spec && \
    cp ~/rpmbuild/RPMS/noarch/rmtrash-${RMTRASH_VERS}-1.noarch.rpm bin/noarch/ && \
    rm -rf rmtrash-${RMTRASH_VERS} && \
    rm -f rmtrash-${RMTRASH_VERS}.tar.gz