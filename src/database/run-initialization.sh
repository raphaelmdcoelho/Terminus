
if [ ! -e /db-started ]
then
# Wait to be sure that SQL Server came up
    echo $TIMEOUT
    sleep $TIMEOUT

# Run the setup script to create the DB and the schema in the DB
# Note: make sure that your password matches what is in the Dockerfile
    for f in ./scripts/*.sql
        do
        echo "$f"
        /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P SqlServer2022* -d master -i $f
    done && touch /db-started
else
    echo "Database already setup"
fi