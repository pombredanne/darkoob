#!/bin/bash

cd ..
grep backends.sqlite darkoob/settings.py
if [ $? -eq 0 ]; then
  rm dardb
  cp dardb darkoob/
else
  grep backends.postgres darkoob/settings.py
  if [ $? -eq 0 ]; then
    dropdb dardb
    createdb dardb
  fi
fi
python darkoob/test/drop_nodes.py
if [ $? -eq 0 ]; then
  python manage.py syncdb
  if [ $? -eq 0 ]; then
    cd darkoob
    python test/test.py
    if [ -f dardb ]; then
      mv dardb ../
    fi
  fi
fi
