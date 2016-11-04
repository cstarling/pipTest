#!/bin/bash

numberOfargs=$#;

if (($numberOfargs<1 )); then
    echo "wrong usage of script... ./omniORBAndomniORBPySetupExtrasForLinux.sh "
else
    activeVirtualEnvirnomentPath=$1;
    cd /$activeVirtualEnvirnomentPath
    touch lib/python2.7/site-packages/omniorb_lib64.pth
    echo "$activeVirtualEnvirnomentPath/omniORB_install/lib64/python2.7/site-packages" > lib/python2.7/site-packages/omniorb_64.pth
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$activeVirtualEnvirnomentPath/omniORB_install/lib

fi