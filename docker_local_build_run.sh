#!/bin/bash

# Check if local.settings.json exists
if [ -f "local.settings.json" ]; then
    # Extract DB2_CONNECTION_STRING value using grep and sed
    DB2_CONNECTION_STRING=$(grep '"DB2_CONNECTION_STRING"' local.settings.json | sed 's/.*: "\(.*\)".*/\1/')

    # Check if the extraction succeeded
    if [ -n "$DB2_CONNECTION_STRING" ]; then
        echo "DB2_CONNECTION_STRING found in local.settings.json."
    else
        echo "DB2_CONNECTION_STRING not found or empty in local.settings.json."
        exit 1
    fi
else
    echo "local.settings.json not found."
    exit 1
fi

# Build the Docker image
docker build -t azure-function-db2-connection .

# Run the Docker container with the extracted DB2_CONNECTION_STRING as an environment variable
docker run -p 8080:80 -e DB2_CONNECTION_STRING="$DB2_CONNECTION_STRING" azure-function-db2-connection