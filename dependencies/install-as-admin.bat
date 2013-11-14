@echo off
@cls

7za.exe x setuptools-1.1.6.tar.gz -so -y | 7za.exe x -si -ttar -y -o"temp"
7za.exe x suds-0.4.tar.gz -so -y | 7za.exe x -si -ttar -y -o"temp"
7za.exe x xlrd-0.9.2.tar.gz -so -y | 7za.exe x -si -ttar -y -o"temp"

pushd temp\setuptools-1.1.6
"%PROGRAMFILES%\Python27\python.exe" setup.py install
popd

pushd temp\suds-0.4
"%PROGRAMFILES%\Python27\python.exe" setup.py install
popd

pushd temp\xlrd-0.9.2
"%PROGRAMFILES%\Python27\python.exe" setup.py install
popd

rmdir /s /q temp
