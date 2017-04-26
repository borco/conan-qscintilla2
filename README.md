## About

*A conan package for [QScintilla2 (GPLv3)](https://www.riverbankcomputing.com/software/qscintilla/download).*

## Usage

### Windows

* add **qmake** dir (for example: `C:\Qt\5.9\mingw53_32\bin`) to your path so that *conan* finds it
* set the default settings to **match it**

```
[settings_defaults]
arch=x86_64
os=Windows
compiler=gcc
compiler.version=5.3
compiler.libcxx=libstdc++11
build_type=Debug
```

### Register to local registry

```
conan export iborco/stable
conan test_package
```

### Remove from local registry

```
conan remove QScintilla2*
```
