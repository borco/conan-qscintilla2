from conans import ConanFile, CMake, tools
from conans.tools import download, unzip
import os

class QscintillaConan(ConanFile):
    name = "QScintilla2"
    description = "QScintilla2 is a port to Qt4/5 of Neil Hodgson's Scintilla C++ editor control."
    version = "0.1"
    license = "GPLv3"
    url = "https://www.riverbankcomputing.com/software/qscintilla/download"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "qmake"
    download_url = "https://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-2.10/QScintilla_gpl-2.10.zip"
    zip_name = "QScintilla_gpl-2.10.zip"
    folder_name = "QScintilla_gpl-2.10/Qt4Qt5"

    def source(self):
        download(self.download_url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        staticlib = "CONFIG+=staticlib" if self.options.shared else ""
        self.run( "cd %s && qmake CONFIG+=debug_and_release %s" % (self.folder_name, staticlib ) )
        if self.settings.build_type == "Debug":
            self.run( "cd %s && make debug" % self.folder_name )
        else:
            self.run( "cd %s && make release" % self.folder_name )

    def package(self):
        self.copy("*.h", dst="include", src="%s" % self.folder_name)
        self.copy("*.h", dst="include/QSci", src="%s/Qsci" % self.folder_name)
        
        self.copy("*libqscintilla2*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["qscintilla2_qt5"]
