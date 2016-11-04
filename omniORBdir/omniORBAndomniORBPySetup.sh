#!/bin/bash          
echo "The number of arguments is: $#";
numberOfargs=$#;

#subprocess.call(['./omniORBdir/omniORBAndomniORBPySetup.sh', activeVirtualEnvirnomentPath, omniorbFileName, omniorbPYFileName,omniORBTarPath,omniORBPYTarPath])

if (($numberOfargs<5)); then
    echo "wrong usage of script... ./omniORBAndomniORBPySetup.sh "
     echo 1st argument: $1;
    echo 2nd argument: $2;
else
    #echo Number of arguments: $#;
    #echo 1st argument: $1;
    #echo 2nd argument: $2;
    #echo 3nd argument: $3;
    #echo 4nd argument: $4;
    #echo 5nd argument: $5;

    activeVirtualEnvirnomentPath=$1;

    omniorbFileName=$2;
    omniorbPYFileName=$3;

    omniORBTarPath=$4
    omniORBPYTarPath=$5

    cd /$activeVirtualEnvirnomentPath;
    ls;

    #echo $omniORBTarPath.tar.bz2;
    cp $omniORBTarPath.tar.bz2 .;
    cp $omniORBPYTarPath.tar.bz2 .;

    tar xvfj $omniorbFileName.tar.bz2;
    tar xvfj $omniorbPYFileName.tar.bz2;

    rm $omniorbFileName.tar.bz2;
    rm $omniorbPYFileName.tar.bz2;

    mkdir omniORB_install

    cd $omniorbFileName
    mkdir build
    cd build

    ../configure --prefix=/$activeVirtualEnvirnomentPath/omniORB_install/ PYTHON=/$activeVirtualEnvirnomentPath/bin/python
    make
    make install


    cd ../../$omniorbPYFileName/
    mkdir build
    cd build
    ../configure --prefix=/$activeVirtualEnvirnomentPath/omniORB_install/ PYTHON=/$activeVirtualEnvirnomentPath/bin/python --with-omniorb=/$activeVirtualEnvirnomentPath/omniORB_install/
    make
    make install


    cd /$activeVirtualEnvirnomentPath

    cp omniORB_install/bin/genior bin/


    touch lib/python2.7/site-packages/omniorb_lib.pth
    touch lib/python2.7/site-packages/omniorb_lib64.pth
    echo "$activeVirtualEnvirnomentPath/omniORB_install/lib/python2.7/site-packages" > lib/python2.7/site-packages/omniorb_lib.pth
    echo "$activeVirtualEnvirnomentPath/omniORB_install/lib64/python2.7/site-packages" > lib/python2.7/site-packages/omniorb_64.pth




fi


