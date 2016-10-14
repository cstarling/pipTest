#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

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
