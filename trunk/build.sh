#!/bin/sh

rm -Rf build
mkdir build

#Make the standalone zip file
cd build 
django-admin startproject data_wrap
cd data_wrap
chmod +x manage.py
cp -f ../../config/*.* .
mkdir Atom2RETS
cp -Rf ../../src/Atom2RETS/*.* Atom2RETS
touch Atom2RETS/__init__.py
mkdir templates
cp -Rf ../../src/templates/*.* templates
cd ..
tar -cvf data-wrap.$1.tar data_wrap
gzip *.tar
zip -r data-wrap.$1.zip data_wrap/
