import logging

from mongodb_driver import mongodb_driver
from logging.handlers import RotatingFileHandler
from datetime import datetime
from db_models import Data_enum, Device_type_enum,RecordxDevices

if __name__ == "__main__":
    # Constants
    HOST = "localhost"
    PORT = 27017
    DB_NAME = "mongodb"
    LOG_FILE_PATH = "mongodb_driver_log.log"

    # Logger
    log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    log_handler = RotatingFileHandler(filename=LOG_FILE_PATH)
    log_handler.setFormatter(log_formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(log_handler)

    # Database Object
    dbinverters = mongodb_driver(host=HOST, port=PORT, db_name=DB_NAME,timeout=1)
    # Insert registers
    # Iterate from  1st to April 26th
    
       
     
        # Define the data for the register
    for day in range(1, 6):
        id = dbinverters.create_id_record()
        data_inv = {
                RecordxDevices.DEVICE_TYPES: "inverter",
                "record_id": id,
                "id_dev": 10140,
                "date": f"2024-06-{day:02d} 08:00:00",
                "gen": 150948.2,
                "ap": 51.958,
                "qp": -34.55,
                "sp": 23.68,
                "pf": 0.91,
                "gen_perc": 100,
                "vac1": 483.4,
                "vac2": 480.2,
                "vac3": 479.7,
                "iac1": 67.694,
                "iac2": 67.66,
                "iac3": 67.666,
                "vdc1": 714.5,
                "idc1": 6.04,
                "os": 512,
                "dev_temp": 68.7,
                "ext_temp": 40,
                "f": 59.987
            }

        data_insert=dbinverters.insert_record( record=data_inv)
        
        # print(data_insert)
        data_fault = {
            "record_id": id,
            "id_dev": data_insert,
            RecordxDevices.DEVICE_TYPES: "fault",
            "date":f"2024-06-{day:02d} 08:00:00",
            "f_code": "E0354",
        }
        # print(data_fault) 
        fault_insert = dbinverters.insert_record(record = data_fault)
        print(fault_insert)
    #lsdata: list = []
    #for day in range(15, 20):
        # Define the data for the register
    #    data = {
    #        "id_device": 10141,
    #        "timestamp": f"2024-05-{day:02d} 08:00:00",
    #        "temp": 25.23,
    #    }

    #    lsdata.append(data)
    
    # Insert the register into the database
    #dbinverters.insert_record(device_type=mongodb_driver_dev_type.TEMP_SENSOR, record=lsdata)
