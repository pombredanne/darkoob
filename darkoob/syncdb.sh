#!/bin/bash

grep backends.sqlite settings.py
if [ $? -eq 0 ]; then
  cd ..
  rm dardb
  python darkoob/test/drop_nodes.py
  python manage.py syncdb
  cp dardb darkoob/
  cd darkoob
  python test/test.py
  mv dardb ../
else
  grep backends.postgres settings.py
  if [ $? -eq 0 ]; then
    dropdb dardb
    createdb dardb
    python ../manage.py syncdb
    python test/test.py
  fi
fi
