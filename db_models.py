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
    VDC1 = "vdc1"
    VDC2 = "vdc2"
    VDC3 = "vdc3"
    VDC4 = "vdc4"
    IDC1 = "idc1"
    IDC2 = "idc2"
    IDC3 = "idc3"
    IDC4 = "idc4"
    OS              = "os"
    DEV_TEMP        = "dev_temp"
    EXT_TEMP        = "ext_temp"
    FREQUENCY       = "f"
    DATE = "date"

    # FAULT
    FAULT_CODE = "f_code"

    # MET SENSORS
    IRRADIANCE = "irr"
    AMBIENT_TEMP = "amb_temp"
    MODULE_TEMP = "mod_temp"

    # MONITORING
    CPU_TEMP = "cpu_temp"
    NET_IFACE = "net_iface"
    NET_TECH = "net_tech"
    RSSI = "rssi"
    RSRP = "rsrp"
    RSRQ = "rsrq"
    LAST_REBOOT = "last_reboot"

    # POWER_METER
    ACTIVE_POWER = "active_power"
    REACTIVE_POWER = "reactive_power"
    APPARENT_POWER = "apparent_power"
    POWER_FACTOR = "power_factor"
    VOLTAGE_A = "voltage_A"
    VOLTAGE_B = "voltage_B"
    VOLTAGE_C = "voltage_C"
    CURRENT_A = "current_A"
    CURRENT_B = "current_B"
    CURRENT_C = "current_C"
    FREQUENCY = "frequency"

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


class MetSensors(str, Enum):
    ID_RECORD = (Data_enum.INSERTED_ID,)
    ID_DEVICE = (Data_enum.ID_DEVICE,)
    SENT = Data_enum.SENT
    DATE = Data_enum.DATE
    DEVICE_TYPES = Data_enum.DEVICE_TYPE
    IRRADIANCE = Data_enum.IRRADIANCE
    AMBIENT_TEMP = Data_enum.AMBIENT_TEMP
    MODULE_TEMP = Data_enum.MODULE_TEMP

    def __str__(self) -> str:
        return self.value


class Faults(str, Enum):
    ID_RECORD       = Data_enum.INSERTED_ID,
    ID_DEVICE       = Data_enum.ID_DEVICE,
    FAULT_CODE      = Data_enum.FAULT_CODE,
    SENT            = Data_enum.SENT
    DATE            = Data_enum.DATE
    DEVICE_TYPES    = Data_enum.DEVICE_TYPE

    def __str__(self) -> str:
        return self.value


class Monitoring(str, Enum):
    ID_RECORD = Data_enum.INSERTED_ID
    ID_DEVICE = Data_enum.ID_DEVICE
    SENT = Data_enum.SENT
    DATE = Data_enum.DATE
    DEVICE_TYPES = Data_enum.DEVICE_TYPE
    CPU_TEMP = Data_enum.CPU_TEMP
    NET_IFACE = Data_enum.NET_IFACE
    NET_TECH = Data_enum.NET_TECH
    RSSI = Data_enum.RSSI
    RSRP = Data_enum.RSRP
    RSRQ = Data_enum.RSRQ
    LAST_REBOOT = Data_enum.LAST_REBOOT

    def __str__(self) -> str:
        return self.value


class Device_type_enum(str, Enum):
    INVERTER            = "inverter"
    FAULT               = "fault"
    MET_SENSOR = "met_sensor"
    MONITORING = "monitoring"
    POWER_METER = "power_meter"

    def __str__(self) -> str:
        return self.value


class Collections(str, Enum):
    RECORDS          = "records",
    INVERTERS        = "inverters"
    FAULTS = "faults"
    MET_SENSORS = "met_sensors"
    MONITORINGS = "monitoring"
    POWER_METERS = "power_meters"

    def __str__(self):
        return self.value
