# Databases

** Terminus

## How to use

1. docker build -t sql-shell .
2. docker run -p 1433:1433 -e TIMEOUT=60 --name sql-shell sql-shell