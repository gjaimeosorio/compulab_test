# ModbusDatabaseDriver
%3CmxGraphModel%3E%3Croot%3E%3CmxCell%20id%3D%220%22%2F%3E%3CmxCell%20id%3D%221%22%20parent%3D%220%22%2F%3E%3CmxCell%20id%3D%222%22%20value%3D%22MongodbDriver%22%20style%3D%22swimlane%3Bhtml%3D1%3BfontStyle%3D1%3Balign%3Dcenter%3BverticalAlign%3Dtop%3BchildLayout%3DstackLayout%3Bhorizontal%3D1%3BstartSize%3D26%3BhorizontalStack%3D0%3BresizeParent%3D1%3BresizeLast%3D0%3Bcollapsible%3D1%3BmarginBottom%3D0%3BswimlaneFillColor%3D%23ffffff%3Brounded%3D0%3Bshadow%3D0%3Bcomic%3D0%3BlabelBackgroundColor%3Dnone%3BstrokeWidth%3D1%3BfillColor%3Dnone%3BfontFamily%3DVerdana%3BfontSize%3D12%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22350%22%20y%3D%22200%22%20width%3D%22220%22%20height%3D%22350%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%223%22%20value%3D%22%2B%20config_path%3A%20str%26lt%3Bdiv%26gt%3B%2B%20config%3A%20str%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%20logger%3A%20Logger%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%26lt%3Bspan%20style%3D%26quot%3Bbackground-color%3A%20initial%3B%26quot%3B%26gt%3B%2B%20database%3A%20Database%26lt%3B%2Fspan%26gt%3B%26lt%3B%2Fdiv%26gt%3B%22%20style%3D%22text%3Bhtml%3D1%3BstrokeColor%3Dnone%3BfillColor%3Dnone%3Balign%3Dleft%3BverticalAlign%3Dtop%3BspacingLeft%3D4%3BspacingRight%3D4%3BwhiteSpace%3Dwrap%3Boverflow%3Dhidden%3Brotatable%3D0%3Bpoints%3D%5B%5B0%2C0.5%5D%2C%5B1%2C0.5%5D%5D%3BportConstraint%3Deastwest%3B%22%20vertex%3D%221%22%20parent%3D%222%22%3E%3CmxGeometry%20y%3D%2226%22%20width%3D%22220%22%20height%3D%2284%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%224%22%20value%3D%22%22%20style%3D%22line%3Bhtml%3D1%3BstrokeWidth%3D1%3BfillColor%3Dnone%3Balign%3Dleft%3BverticalAlign%3Dmiddle%3BspacingTop%3D-1%3BspacingLeft%3D3%3BspacingRight%3D3%3Brotatable%3D0%3BlabelPosition%3Dright%3Bpoints%3D%5B%5D%3BportConstraint%3Deastwest%3B%22%20vertex%3D%221%22%20parent%3D%222%22%3E%3CmxGeometry%20y%3D%22110%22%20width%3D%22220%22%20height%3D%228%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%225%22%20value%3D%22%26lt%3Bdiv%26gt%3B%2B%20post_init%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bsetup_logging%3A%20none%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%20get_database_client%3A%20Database%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bcreate_id_record%3A%20str%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Binsert_device_record%3A%20str%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bget_record_by_id%3A%20str%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bget_all_records%3A%20list%5Bdict%5D%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bget_unsent_records%3A%20list%5Bdict%5D%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%26amp%3Bnbsp%3Bupdate_records_by_id%3A%20bool%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%26lt%3Bspan%20style%3D%26quot%3Bbackground-color%3A%20initial%3B%26quot%3B%26gt%3B%2B%20delete_record_by_id%3A%20bool%26lt%3B%2Fspan%26gt%3B%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%26lt%3Bdiv%26gt%3B%2B%20delete_record_by_date%3A%20bool%26lt%3B%2Fdiv%26gt%3B%26lt%3B%2Fdiv%26gt%3B%26lt%3Bdiv%26gt%3B%26lt%3Bbr%26gt%3B%26lt%3B%2Fdiv%26gt%3B%22%20style%3D%22text%3Bhtml%3D1%3BstrokeColor%3Dnone%3BfillColor%3Dnone%3Balign%3Dleft%3BverticalAlign%3Dtop%3BspacingLeft%3D4%3BspacingRight%3D4%3BwhiteSpace%3Dwrap%3Boverflow%3Dhidden%3Brotatable%3D0%3Bpoints%3D%5B%5B0%2C0.5%5D%2C%5B1%2C0.5%5D%5D%3BportConstraint%3Deastwest%3B%22%20vertex%3D%221%22%20parent%3D%222%22%3E%3CmxGeometry%20y%3D%22118%22%20width%3D%22220%22%20height%3D%22182%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3C%2Froot%3E%3C%2FmxGraphModel%3E
`ModbusDatabaseDriver` is a class that interacts with a MongoDB database to manage Modbus records and devices. Below is a description of each method in the class and its functionality.

## Table of Contents
- [Initialization](#initialization)
- [Private Methods](#private-methods)
- [Public Methods](#public-methods)
- [Usage Example](#usage-example)

## Initialization

### `__post_init__()`
This method is automatically called after the object initialization. It sets up the configuration file, logging system, and establishes the MongoDB database connection.

**Description:**
- Purpose: Initializes the configuration, logging system, and database connection.
- Attributes:
  - `config_path`: Path to the configuration file.
  - `config`: Configuration read from the `config_path`.
  - `database`: MongoDB client database.

## Private Methods

### `_setup_logging()`
Sets up the logging system based on the provided configurations in the configuration file.

**Description:**
- Purpose: Configure the logging level and destination (file, stdout).
- Attributes:
  - `loglevel`: Logging level.
  - `logstdout`: Indicator for logging to stdout.
  - `logfile`: Log file.

### `_get_database_client()`
Establishes the connection to the MongoDB client using the provided configurations.

**Description:**
- Purpose: Connect to the MongoDB database.
- Attributes:
  - `host`: Database host.
  - `port`: Database port.
  - `database_name`: Database name.

### `_get_all_records()`
Retrieves all records from the specified collection.

**Description:**
- Purpose: Retrieve all records from a collection.
- Attributes:
  - `collection_name`: Name of the collection.
  - `val_return`: List of obtained records.

## Public Methods

### `create_id_record()`
Creates a new ID record in the database.

**Description:**
- Purpose: Generate a new ID for a record.
- Attributes:
  - `collection_name`: Name of the records collection.
  - `id_record`: ID of the new record.

### `insert_device_record(device_data)`
Inserts a new device record into the database.

**Description:**
- Purpose: Insert device data.
- Attributes:
  - `device_data`: Data of the device to insert.
  - `inserted_id`: ID of the inserted record.

### `get_all_records()`
Retrieves all records from the devices collection.

**Description:**
- Purpose: Retrieve all device records.
- Attributes:
  - `collection_name`: Name of the devices collection.
  - `val_return`: List of device records.

### `get_all_device_unsent()`
Retrieves all unsent device records.

**Description:**
- Purpose: Retrieve unsent device records.
- Attributes:
  - `collection_name`: Name of the devices collection.
  - `val_return`: List of unsent records.

### `update_device_data(id_record, device_type, new_data)`
Updates a specific device record.

**Description:**
- Purpose: Update the data of a device.
- Attributes:
  - `id_record`: ID of the record to update.
  - `device_type`: Type of device.
  - `new_data`: Updated device data.
  - `val_return`: Success indicator of the update.

### `delete_device_by_id_record(id_record, device_type)`
Deletes a device record by ID.

**Description:**
- Purpose: Delete a device record by its ID.
- Attributes:
  - `id_record`: ID of the record to delete.
  - `device_type`: Type of device.
  - `val_return`: Success indicator of the deletion.

### `delete_device_by_date(start_date, end_date, device_type)`
Deletes device records by date range.

**Description:**
- Purpose: Delete device records within a date range.
- Attributes:
  - `start_date`: Start date of the range.
  - `end_date`: End date of the range.
  - `device_type`: Type of device.
  - `val_return`: Success indicator of the deletion.

### `get_device_by_id_record(id_record)`
Retrieves a device record by its ID.

**Description:**
- Purpose: Retrieve a device record by its ID.
- Attributes:
  - `id_record`: ID of the record to retrieve.
  - `val_return`: Retrieved device record.

## Usage Example

### Driver Initialization
```python
from modbus_database_driver import ModbusDatabaseDriver

# Initialize the driver with the configuration file path
driver = ModbusDatabaseDriver(config_path="path/to/config.ini")


# Create a new record and obtain its ID
record_id = driver.create_id_record()
print(f"Created record ID: {record_id}")


# Insert a new device record
device_record = {
    "device_type": "INVERTER",
    "data": "sample data"
}
inserted_id = driver.insert_device_record(device_record)
print(f"Inserted device record ID: {inserted_id}")


# Get all records
all_records = driver.get_all_records()
print(f"All records: {all_records}")


# Get all unsent device records
unsent_records = driver.get_all_device_unsent()
print(f"Unsent device records: {unsent_records}")


# Update a device record
update_data = {"new_data": "updated data"}
update_success = driver.update_device_data(record_id, "INVERTER", update_data)
print(f"Update success: {update_success}")


# Delete a device record by ID
delete_success = driver.delete_device_by_id_record(record_id, "INVERTER")
print(f"Delete success: {delete_success}")


# Delete device records by date range
delete_by_date_success = driver.delete_device_by_date("2023-01-01", "2023-12-31", "INVERTER")
print(f"Delete by date success: {delete_by_date_success}")


# Get a device record by ID
device_record = driver.get_device_by_id_record(record_id)
print(f"Device record: {device_record}")
```
