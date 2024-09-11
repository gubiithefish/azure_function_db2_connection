import azure.functions as func
from datetime import datetime
import logging
import ibm_db
import os

# Create a FunctionApp instance
app = func.FunctionApp()

# Environment variable for the DB2 connection string
db_connection_string = os.getenv("DB2_CONNECTION_STRING")


@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for /HttpExample endpoint.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            body=("This HTTP triggered function executed successfully. "
                  "Pass a name in the query string or in the request body for a personalized response."),
            status_code=200
        )


@app.route(route="Db2Test", auth_level=func.AuthLevel.ANONYMOUS)
def Db2Test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for "/db-test" endpoint.')

    if db_connection_string is None:
        logging.error("DB2_CONNECTION_STRING environment variable is not set.")
        return func.HttpResponse("DB2 connection string not found.", status_code=500)

    try:
        # Connect to the DB2 database
        conn = ibm_db.connect(db_connection_string, "", "")

        # Query to get the current date from sysibm.sysdummy1
        query_datetime = "SELECT CURRENT_DATE AS SYSTEM_DATE, CURRENT_TIME AS SYSTEM_TIME FROM SYSIBM.SYSDUMMY1"
        result_datetime = ibm_db.fetch_assoc(ibm_db.exec_immediate(conn, query_datetime))
        date = datetime.strptime(str(result_datetime['SYSTEM_DATE']), '%Y-%m-%d').strftime('%Y-%m-%d')
        time = datetime.strptime(str(result_datetime['SYSTEM_TIME']), '%H:%M:%S').strftime('%H:%M:%S')

        # Query to get the DB2 version from sysibmadm.env_inst_info
        query_version = "SELECT SERVICE_LEVEL FROM SYSIBMADM.ENV_INST_INFO"
        result_version = ibm_db.fetch_assoc(ibm_db.exec_immediate(conn, query_version))
        service_version = result_version['SERVICE_LEVEL']

        # Close the connection
        ibm_db.close(conn)

        # Format the response message
        message = (f"DB2 System Date: {date}, "
                   f"System Time: {time}, "
                   f"Service Level: {service_version}")

        # Return the result as a response
        return func.HttpResponse(body=message, status_code=200)

    except Exception as e:
        logging.error(f"Error querying DB2: {e}")
        return func.HttpResponse(f"Error querying DB2: {str(e)}", status_code=500)
