from enum import Enum
from enum import auto


class Data_enum(str, Enum):
    ID_RECORD       = "_id",
    TIMESTAMP       = "ts",
    SENT            = "sent",
    DEVICE_TYPE     = "dev_type",
    INSERTED_ID     = "record_id"

    # INVERTER
    ID_DEVICE       = "id_dev" #evice id = device serial
    GEN             = "gen"
    ACTIVE_POWER    = "ap"
    REACTIVE_POWER  = "qp"
    APPARENT_POWER  = "sp"
    POWER_FACTOR    = "pf"
    GEN_PERCENTAGE  = "gen_perc"
    VAC1            = "vac1"
    VAC2            = "vac2"
    VAC3            = "vac3"
    IAC1            = "iac1"
    IAC2            = "iac2"
    IAC3            = "iac3"
    VDC             = "vdc1"
    IDC             = "idc1"
    OS              = "os"
    DEV_TEMP        = "dev_temp"
    EXT_TEMP        = "ext_temp"
    FREQUENCY       = "f"
    DATE           = "date"

    #FAULT
    FAULT_CODE          = "f_code"

    def __str__(self) -> str:
        return self.value


class Records(str, Enum):
    ID_RECORD       = Data_enum.ID_RECORD,
    TIMESTAMP       = Data_enum.TIMESTAMP

    def __str__(self) -> str:
        return self.value


class Inverters(str, Enum):
    
    ID_RECORD       = Data_enum.INSERTED_ID,
    ID_DEVICE       = Data_enum.ID_DEVICE,
    GEN             = Data_enum.GEN
    SEND            = Data_enum.SENT
    ACTIVE_POWER    = Data_enum.ACTIVE_POWER
    REACTIVE_POWER  = Data_enum.REACTIVE_POWER
    APPARENT_POWER  = Data_enum.APPARENT_POWER
    POWER_FACTOR    = Data_enum.POWER_FACTOR
    GEN_PERCENTAGE  = Data_enum.GEN_PERCENTAGE
    VAC1            = Data_enum.VAC1
    VAC2            = Data_enum.VAC2
    VAC3            = Data_enum.VAC3
    IAC1            = Data_enum.IAC1
    IAC2            = Data_enum.IAC2
    IAC3            = Data_enum.IAC3
    VDC             = Data_enum.VDC
    IDC             = Data_enum.IDC
    OS              = Data_enum.OS
    DEV_TEMP        = Data_enum.DEV_TEMP
    EXT_TEMP        = Data_enum.EXT_TEMP
    DATE            = Data_enum.DATE
    DEVICE_TYPES    = Data_enum.DEVICE_TYPE

    def __str__(self) -> str:
        return self.value


# class RecordxDevices(str, Enum):
#     ID_RECORD        = Data_enum.INSERTED_ID
#     ID_DEVICE        = Data_enum.ID_DEVICE,
#     DEVICE_TYPES     = Data_enum.DEVICE_TYPE,
#     SENT             = Data_enum.SENT

#     def __str__(self) -> str:
#         return self.value


class Faults(str, Enum):
    ID_RECORD       = Data_enum.INSERTED_ID,
    ID_DEVICE       = Data_enum.ID_DEVICE,
    FAULT_CODE      = Data_enum.FAULT_CODE,
    SENT            = Data_enum.SENT
    DATE            = Data_enum.DATE
    DEVICE_TYPES    = Data_enum.DEVICE_TYPE

    def __str__(self) -> str:
        return self.value

class Device_type_enum(str, Enum):
    INVERTER            = "inverter"
    FAULT               = "fault"

    def __str__(self) -> str:
        return self.value


class Collections(str, Enum):
    RECORDS          = "records",
    INVERTERS        = "inverters"
    FAULTS           = "fault"


    def __str__(self):
        return self.value
