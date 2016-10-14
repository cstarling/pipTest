#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install
import subprocess
import sys
import os
class install(_install):
    def pre_install_script(self):
        print "in pre install"
        omniORBinPath = False
        for path in sys.path:
            if "omniORB" not in path:
                continue
            else:
                omniORBinPath = True

        if omniORBinPath == False:
            omniorbFileName = 'omniORB-4.2.1'
            omniorbPYFileName = 'omniORBpy-4.2.1'
            activeVirtualEnvirnomentPath = sys.exec_prefix

            omniORBTarPath = (os.path.dirname(os.path.realpath(__file__)) + '/DCM_IIOP/omniORBdir/' + omniorbFileName)

            omniORBPYTarPath = (os.path.dirname(os.path.realpath(__file__)) + '/DCM_IIOP/omniORBdir/' + omniorbPYFileName)
            print "py tar" , omniORBPYTarPath

            subprocess.call(['./DCM_IIOP/omniORBdir/omniORBAndomniORBPySetup.sh', activeVirtualEnvirnomentPath, omniorbFileName,
                             omniorbPYFileName, omniORBTarPath, omniORBPYTarPath])

            print "it is not on path"
        else:
            print "it is on the path"


    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'DCM_IIOP',
        version = '1.0.dev0',
        description = '''''',
        long_description = '''''',
        author = "",
        author_email = "",
        license = '',
        url = '',
        #scripts = ['DCM_IIOP/DCM_idl.py',
        #           'DCM_IIOP/DCM_Types_idl.py'
       #            ],
        packages = [
            'DCM_IIOP',
            'DCM_IIOP.DCM',
            'DCM_IIOP.DCM__POA',
            'DCM_IIOP._GlobalIDL',
            'DCM_IIOP._GlobalIDL__POA',
        ],
        py_modules = [],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe=True,
        cmdclass={'install': install},
    )
