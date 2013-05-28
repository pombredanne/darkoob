Darkoob
=======
** A SOCIAL ** 

Installation
------------

Requirement
------------
Download and unzip the latest Elasticsearch distribution on http://www.elasticsearch.org/download/
Run bin/elasticsearch -f on Unix,
or bin/elasticsearch.bat on Windows
Run curl -X GET http://localhost:9200/

WIKI
----

--------------------------
SEARCH ENGINE INSTALLATION
--------------------------

INSTALLING MEMCACHED
---------------------
DOWNLOAD: http://memcached.googlecode.com/files/memcached-1.4.15.tar.gz
RUN:
  *./configure
  *sudo make
  *sudo make install
Run: python manage.py rebuild_index
