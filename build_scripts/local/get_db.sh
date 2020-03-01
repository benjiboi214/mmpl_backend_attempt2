#!/bin/bash\

./build_scripts/local/stop.sh

## Gets Data from remote PSQL instance
ssh ben@vpn.systemiphus.com /bin/bash << EOF
    export PGHOST=terraform-20200208074413765400000001.cresquhkubnp.ap-southeast-2.rds.amazonaws.com;
    export PGPASSWORD=b5z8YJZFA8tgk3Z3nS7z;
    export PGDATABASE=mmpl_backend_staging;
    export PGUSER=mmpl_backend;
    pg_dump -O > export.sql;
    ls -la;
EOF

# Copies Data to local FS
scp ben@vpn.systemiphus.com:~/export.sql  ./export.sql

export PGDATABASE=mmpl_backend
export PGUSER=mmpl_backend

# Drops DB named as current branch if exists
DB_NAME=`git rev-parse --abbrev-ref HEAD | sed 's/\//_/'`
echo "Putting DB in: $DB_NAME"
psql -c "drop database $DB_NAME;"

# Create target DB
psql -c "create database $DB_NAME with owner $PGUSER encoding = 'UNICODE';"

# Restores DB from dump
psql -U $PGUSER -d $DB_NAME -f export.sql