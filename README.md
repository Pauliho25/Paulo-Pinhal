# Paulo-Pinhal
# Backup Cloud Tool

## Introducción

**Backup Cloud Tool** es una aplicación diseñada para realizar respaldos automáticos de archivos locales a servicios de almacenamiento en la nube como OneDrive. Este proyecto incluye un script que genera un ejecutable capaz de realizar copias de seguridad de archivos o directorios especificados a una cuenta de OneDrive u otros servicios de almacenamiento en la nube compatibles. 

Este proyecto es útil para quienes necesitan mantener una copia de seguridad en la nube de sus datos importantes de manera sencilla y automática.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Dependencias](#dependencias)
- [Características](#características)
- [Ejemplos](#ejemplos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

### Requisitos previos

- Python 3.x
- Cuenta en OneDrive (o cualquier otro servicio de nube compatible)
- Acceso a una terminal o línea de comandos

### Pasos de instalación

1. Clona el repositorio del proyecto:
    ```bash
    git clone https://github.com/usuario/backup-cloud-tool.git
    cd backup-cloud-tool
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. (Opcional) Genera el ejecutable (si es necesario):
    ```bash
    pyinstaller --onefile backup_script.py
    ```

## Configuración

### Configurar OneDrive (u otro servicio de nube)

Antes de usar el programa, debes configurar las credenciales de acceso a tu servicio de almacenamiento en la nube. Para OneDrive, se puede utilizar la API de Microsoft Graph:

1. Registra una aplicación en el [portal de Azure](https://portal.azure.com) y obtén las credenciales (client ID, secret y redirect URI).
2. Coloca las credenciales en un archivo de configuración o como variables de entorno. Ejemplo de un archivo `.env`:
    ```bash
    ONEDRIVE_CLIENT_ID=tu_client_id
    ONEDRIVE_CLIENT_SECRET=tu_client_secret
    ONEDRIVE_REDIRECT_URI=tu_redirect_uri
    ```

3. Modifica el script para usar estas variables o el archivo de configuración.

### Configuración de otros servicios en la nube

Si prefieres utilizar otro servicio de almacenamiento en la nube, debes ajustar el script para que utilice la API del servicio correspondiente (por ejemplo, Google Drive, Dropbox, etc.).

## Uso

### Ejecutar el script

Si no has creado un ejecutable, puedes ejecutar el script directamente con Python:
```bash
python backup_script.py
