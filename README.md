# ModbusDatabaseDriver

`ModbusDatabaseDriver` es una clase que interactúa con una base de datos MongoDB para gestionar registros y dispositivos Modbus. A continuación se describe cada método de la clase y su funcionalidad.

## Tabla de Contenidos
- [Inicialización](#inicialización)
- [Métodos Privados](#métodos-privados)
- [Métodos Públicos](#métodos-públicos)
- [Ejemplo de Uso](#ejemplo-de-uso)

## Inicialización

### `__post_init__()`
Este método se llama automáticamente después de la inicialización del objeto. Configura el archivo de configuración, el registro y establece la conexión a la base de datos MongoDB.

**Descripción:**
- Propósito: Inicializa la configuración, el sistema de registro y la conexión a la base de datos.
- Atributos:
  - `config_path`: Ruta del archivo de configuración.
  - `config`: Configuración leída del archivo `config_path`.
  - `database`: Cliente de la base de datos MongoDB.

## Métodos Privados

### `_setup_logging()`
Configura el sistema de registro según las configuraciones proporcionadas en el archivo de configuración.

**Descripción:**
- Propósito: Configurar el nivel y destino del registro (archivo, stdout).
- Atributos:
  - `loglevel`: Nivel de registro.
  - `logstdout`: Indicador de registro en stdout.
  - `logfile`: Archivo de registro.

### `_get_database_client()`
Establece la conexión con el cliente de la base de datos MongoDB utilizando las configuraciones proporcionadas.

**Descripción:**
- Propósito: Conectar con la base de datos MongoDB.
- Atributos:
  - `host`: Host de la base de datos.
  - `port`: Puerto de la base de datos.
  - `database_name`: Nombre de la base de datos.

### `_get_all_records()`
Obtiene todos los registros de la colección especificada.

**Descripción:**
- Propósito: Obtener todos los registros de una colección.
- Atributos:
  - `collection_name`: Nombre de la colección.
  - `val_return`: Lista de registros obtenidos.

## Métodos Públicos

### `create_id_record()`
Crea un nuevo registro de ID en la base de datos.

**Descripción:**
- Propósito: Generar un nuevo ID para un registro.
- Atributos:
  - `collection_name`: Nombre de la colección de registros.
  - `id_record`: ID del nuevo registro.

### `insert_device_record(device_data)`
Inserta un nuevo registro de dispositivo en la base de datos.

**Descripción:**
- Propósito: Insertar datos de un dispositivo.
- Atributos:
  - `device_data`: Datos del dispositivo a insertar.
  - `inserted_id`: ID del registro insertado.

### `get_all_records()`
Obtiene todos los registros de la colección de dispositivos.

**Descripción:**
- Propósito: Obtener todos los registros de dispositivos.
- Atributos:
  - `collection_name`: Nombre de la colección de dispositivos.
  - `val_return`: Lista de registros de dispositivos.

### `get_all_device_unsent()`
Obtiene todos los registros de dispositivos que no han sido enviados.

**Descripción:**
- Propósito: Obtener registros de dispositivos no enviados.
- Atributos:
  - `collection_name`: Nombre de la colección de dispositivos.
  - `val_return`: Lista de registros no enviados.

### `update_device_data(id_record, device_type, new_data)`
Actualiza un registro de dispositivo específico.

**Descripción:**
- Propósito: Actualizar los datos de un dispositivo.
- Atributos:
  - `id_record`: ID del registro a actualizar.
  - `device_type`: Tipo de dispositivo.
  - `new_data`: Datos actualizados del dispositivo.
  - `val_return`: Indicador de éxito de la actualización.

### `delete_device_by_id_record(id_record, device_type)`
Elimina un registro de dispositivo por ID.

**Descripción:**
- Propósito: Eliminar un registro de dispositivo por su ID.
- Atributos:
  - `id_record`: ID del registro a eliminar.
  - `device_type`: Tipo de dispositivo.
  - `val_return`: Indicador de éxito de la eliminación.

### `delete_device_by_date(start_date, end_date, device_type)`
Elimina registros de dispositivos por rango de fechas.

**Descripción:**
- Propósito: Eliminar registros de dispositivos dentro de un rango de fechas.
- Atributos:
  - `start_date`: Fecha de inicio del rango.
  - `end_date`: Fecha de fin del rango.
  - `device_type`: Tipo de dispositivo.
  - `val_return`: Indicador de éxito de la eliminación.

### `get_device_by_id_record(id_record)`
Obtiene un registro de dispositivo por su ID.

**Descripción:**
- Propósito: Obtener un registro de dispositivo por su ID.
- Atributos:
  - `id_record`: ID del registro a obtener.
  - `val_return`: Registro del dispositivo obtenido.

## Ejemplo de Uso

### Inicialización del Driver
```python
from modbus_database_driver import ModbusDatabaseDriver

# Inicializar el driver con la ruta del archivo de configuración
driver = ModbusDatabaseDriver(config_path="path/to/config.ini")


# Crear un nuevo registro y obtener su ID
record_id = driver.create_id_record()
print(f"Created record ID: {record_id}")


# Insertar un nuevo registro de dispositivo
device_record = {
    "device_type": "INVERTER",
    "data": "sample data"
}
inserted_id = driver.insert_device_record(device_record)
print(f"Inserted device record ID: {inserted_id}")


# Obtener todos los registros
all_records = driver.get_all_records()
print(f"All records: {all_records}")


# Obtener todos los registros de dispositivos no enviados
unsent_records = driver.get_all_device_unsent()
print(f"Unsent device records: {unsent_records}")



# Actualizar un registro de dispositivo
update_data = {"new_data": "updated data"}
update_success = driver.update_device_data(record_id, "INVERTER", update_data)
print(f"Update success: {update_success}")



# Eliminar un registro de dispositivo por ID
delete_success = driver.delete_device_by_id_record(record_id, "INVERTER")
print(f"Delete success: {delete_success}")



# Eliminar registros de dispositivos por rango de fechas
delete_by_date_success = driver.delete_device_by_date("2023-01-01", "2023-12-31", "INVERTER")
print(f"Delete by date success: {delete_by_date_success}")




# Obtener un registro de dispositivo por ID
device_record = driver.get_device_by_id_record(record_id)
print(f"Device record: {device_record}")
```
