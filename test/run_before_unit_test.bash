#!/bin/bash
cd ..
python -c "import sys;print(sys.version)"
python setup.py build
python setup.py install --install-platlib test/.
