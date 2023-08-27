#!/bin/bash
# Run Microsoft SQl Server and initialization script (at the same time)
/usr/src/app/run-initialization.sh & /opt/mssql/bin/sqlservr

#Note: server command must be after &, otherwise Docker container will stop when run-initialization.sh script finishes job. In example referenced by Microsoft this order is reversed, but container works because of node.js server running.
#Note2: be sure that you pass to Docker image script files with Unix line endings, otherwise you may encounter strange bugs.