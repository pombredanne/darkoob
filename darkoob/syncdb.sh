#!/bin/bash

grep backends.sqlite settings.py
if [ $? -eq 0 ]; then
  rm dardb
else
  grep backends.postgres settings.py
  if [ $? -eq 0 ]; then
    dropdb dardb
    createdb dardb
  fi
fi
python test/drop_nodes.py
if [ $? -eq 0 ]; then
  python ../manage.py syncdb
  if [ $? -eq 0 ]; then
    python test/test.py
  fi
fi
