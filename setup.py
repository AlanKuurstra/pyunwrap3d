from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_setuptools_version

#this method fails if numpy is not yet installed, instead override the build_ext command
#import numpy
#includeDirs = numpy.get_include()

extensions = []
extensions.append(
    Extension('pyunwrap3d',
              sources=['unwrap3dInterface.cpp'],
              #include_dirs=[numpy.get_include()],
              #install_requires=['numpy']
              )
    )

class build_ext(build_ext_setuptools_version):
    def run(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        build_ext_setuptools_version.run(self)

setup(
    name="pyunwrap3d",
    version="0.3",
    description = "Python interface to unwrap3d",
    cmdclass={'build_ext':build_ext},
    setup_requires=['numpy'],
    install_requires=['numpy'],
    ext_modules=extensions)
