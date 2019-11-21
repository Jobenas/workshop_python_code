import logging
import pymysql
import azure.functions as func

def insert_vals_into_db(devID, contVal, discVal):
    host = "iot.jobenas.com"
    user = "iotuser"
    passwd = "10tp45sw0rd"
    db = "iot"

    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = conn.cursor()

    query = f"INSERT INTO example_table (sensor_id, sensor_value_cont, sensor_value_disc) VALUES ({devID}, {contVal}, {discVal})"

    try:
        cursor.execute(query)
        conn.commit()

        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    devID = req.params.get('devId')
    contVal = req.params.get("contVal")
    discVal = req.params.get("discVal")
    if (not devID) and (not contVal) and (not discVal):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            devID = req_body.get('devId')
            contVal = req_body.get("contVal")
            discVal = req_body.get("discVal")

    if devID and contVal and discVal:
        result = insert_vals_into_db(devID, contVal, discVal)

        if result:
            return func.HttpResponse(f"Values inserted successfully into db")
        else:
            return func.HttpResponse(f"Some Error happened during operation")
    else:
        return func.HttpResponse(
             "Please use a post request with the values for sensor",
             status_code=400
        )
