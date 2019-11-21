import logging
import pymysql
import azure.functions as func

def insert_vals_into_db(devId, button_state, timestamp):
    host = "iot.jobenas.com"
    user = "iotuser"
    passwd = "10tp45sw0rd"
    db = "iot"

    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = conn.cursor()

    query = f"INSERT INTO button_example_table (state, timestamp, sensor_id) VALUES({button_state}, '{timestamp}', {devId})"

    try:
        cursor.execute(query)
        conn.commit()

        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    devId = None
    timestamp = None
    button_state = None

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        devId = req_body.get("devId")
        timestamp = req_body.get("timestamp")
        button_state = req_body.get("buttonState")

    if devId and timestamp and button_state:
        result = insert_vals_into_db(devId, button_state, timestamp)

        if result:
            return func.HttpResponse(f"Values inserted successfully into db")
        else:
            return func.HttpResponse(f"Some Error happened during operation")
    else:
        return func.HttpResponse(
            "Please use a POST request with the values in JSON format",
            status_code=400
        )