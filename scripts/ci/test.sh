#!/bin/bash
mkdir -p build
env/bin/pylint --reports=n --rcfile=config/pylint.rc --output-format=parseable paragon/*/ > build/python-lint.txt ||:
cd paragon && ../env/bin/python manage.py test --with-xunit --xunit-file=../build/python-tests.xml
