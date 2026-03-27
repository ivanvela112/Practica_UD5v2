# Entrega práctica – Comprobaciones del dominio

**Nombre alumno:**  
**Nombre del dominio:**  

---

## 1. Estructura del dominio, DC y equipos desde DC1

**Comando**

```
Get-ADComputer -Filter * | Select Name,OperatingSystem
```

**Salida**

```
DC01
DC02
FS01
CLIENT01
CLIENT02
CLIENT03
```

## 2. Estructura de ficheros en D: desde el DC1

**Comando**

```
tree \\FS01\empresa
```

**Salida**

```
\\FS01\EMPRESA.
├──comerciales
│  ├──comercial1
│  └──comercial2
├──comun
├──direccion
├──perfiles
└──tecnicos
   ├──tecnico1
   │  └──prueba
   └──tecnico2

```

---

## 3. Uds. Organizativas, usuarios y grupos del dominio

### Unidades Organizativas

**Comando**

```
Get-ADOrganizationalUnit -Filter * | Select Name
Get-ADUser -Filter * | Select Name
Get-ADGroup -Filter * | Select Name
```

**Salida**
```
Domain Controllers
OU_Tecnicos
OU_Comerciales
OU_Equipos
Administrador
tecnico1
tecnico2
comercial1
comercial2
adm_dominio
adm_fileserver
Administradores

Usuarios
Invitados
Opers. de impresión
Operadores de copia de seguridad
Duplicadores
Usuarios de escritorio remoto
Operadores de configuración de red
Usuarios del monitor de sistema
Usuarios del registro de rendimiento
Usuarios COM distribuidos
IIS_IUSRS
Operadores criptográficos
Lectores del registro de eventos
Acceso DCOM a Serv. de certif.
Servidores de acceso remoto RDS
Servidores de extremo RDS
Servidores de administración RDS
Administradores de Hyper-V
Operadores de asistencia de control de acceso
Usuarios de administración remota
Storage Replica Administrators
Usuarios de OpenSSH
Equipos del dominio
Controladores de dominio
Administradores de esquema
Administradores de empresas
Publicadores de certificados
Admins. del dominio
Usuarios del dominio
Invitados del dominio
Propietarios del creador de directivas de grupo
Servidores RAS e IAS
Opers. de servidores
Opers. de cuentas
Acceso compatible con versiones anteriores de Windows 2000
Creadores de confianza de bosque de entrada
Grupo de acceso de autorización de Windows
Servidores de licencias de Terminal Server
Grupo de replicación de contraseña RODC permitida
Grupo de replicación de contraseña RODC denegada
Controladores de dominio de sólo lectura
Enterprise Domain Controllers de sólo lectura
Controladores de dominio clonables
Protected Users
Administradores clave
Administradores clave de la organización
Cuentas de confianza de bosque
Cuentas de confianza externas
DnsAdmins
DnsUpdateProxy
GG_Tecnicos
GG_Comerciales

```
---

## 4. Carpetas V6 de los perfiles móviles

**Comando**

```
Get-ADUser -Filter * -Properties ProfilePath | Select Name, ProfilePath
```

**Salida**
```
Administrador
tecnico1 \\FS01\perfiles\tecnico1
tecnico2 \\FS01\perfiles\tecnico2
comercial1 \\FS01\perfiles\comercial1
comercial2 \\FS01\perfiles\comercial2
adm_dominio
adm_fileserver

```
---

## 5. Comprobación carpetas compartidas, cada usuario la suya. Demostrar la estructura de permisos de esta. Incluida SAMBA

### Permisos carpeta usuario

**Comando**

```
Get-Acl D:\empresa\tecnico
Get-ChildItem \FS01\usuarios | Select Name
ssh usuario@CLIENT03 "ls /etc/fstab"
```

**Salida**
```
Directorio: D:\empresa

Path: tecnicos
Owner: BUILTIN\Administradores
Access: CREATOR OWNER Allow  FullControl...
Administrador
adm_fileserver
Public
salida

```
---

## 6. Comprobación GPOs funcionando

**Comando**

```
gpresult /r
```

**Salida**
```
# ========================================================
# REPORTE INTEGRADO DE CONFIGURACIÓN AD Y GPO (RSOP)
# ========================================================

# 1. DATOS DEL USUARIO EN ACTIVE DIRECTORY 
$adUser = [PSCustomObject]@{
    DistinguishedName = "CN=comercial1,OU=OU_Comerciales,DC=ivl,DC=local"
    SamAccountName    = "comercial1"
    UserPrincipalName = "comercial1@ivl.local"
    ObjectGUID        = "5668febf-b9c0-4a29-bc5d-bcf12debfa55"
    SID               = "S-1-5-21-8228041-1025387836-864803159-1605"
    Enabled           = $true
}

# 2. CONFIGURACIÓN GENERAL DEL EQUIPO 
$equipoConfig = [PSCustomObject]@{
    NombreEquipo      = "DC01"
    VersionSO         = "10.0.26100"
    Sitio             = "Default-First-Site-Name"
    DN_Equipo         = "CN=DC01,OU=Domain Controllers,DC=ivl,DC=local"
    Dominio           = "IVL (Windows 2008 o posterior)"
    GPOs_Aplicadas    = @(
        "Default Domain Controllers Policy",
        "Default Domain Policy"
    )
    Grupos_Seguridad  = @(
        "Administradores", "Todos", "Usuarios", "NT AUTHORITY\NETWORK",
        "Usuarios autenticados", "Controladores de dominio", 
        "NT AUTHORITY\ENTERPRISE DOMAIN CONTROLLERS"
    )
}

# 3. CONFIGURACIÓN DE LA SESIÓN DE USUARIO (Imagen 4 y 5)
$usuarioSesion = [PSCustomObject]@{
    DN_Usuario        = "CN=Administrador,CN=Users,DC=ivl,DC=local"
    UltimaAplicacion  = "27/03/2026 13:35:24"
    GPOs_Aplicadas    = @(
        "GPO Fondo Pantalla",
        "GPO_Restriccion_PanelControl"
    )
    # Listado completo unificado de grupos (Incluyendo la última imagen)
    Membresia_Grupos  = @(
        "Usuarios del dominio",
        "Todos",
        "Administradores",
        "Usuarios",
        "Acceso compatible con versiones anteriores de Windows 2000",
        "NT AUTHORITY\INTERACTIVE",
        "INICIO DE SESIÓN EN LA CONSOLA",
        "Usuarios autenticados",
        "Esta compañía",
        "LOCAL",
        "Propietarios del creador de directivas de grupo",
        "Admins. del dominio",
        "Administradores de empresas",
        "Administradores de esquema",
        "Identidad afirmada de la autoridad de autenticación",
        "Grupo de replicación de contraseña RODC denegada",
        "Nivel obligatorio alto"
    )
}


```
---

## 7. Restricciones de logging

**Comando**

```
Get-ADUser comercial1 -Properties LogonHours,LogonWorkstations
```

**Salida**
```

    DistinguishedName  = "CN=comercial1,OU=OU_Comerciales,DC=ivl,DC=local"
    Enabled            = $true
    GivenName          = "comercial1"
    LogonHours         = @(0, 31, 0, 0) # Valores truncados en la imagen
    LogonWorkstations  = ""
    Name               = "comercial1"
    ObjectClass        = "user"
    ObjectGUID         = "5668febf-b9c0-4a29-bc5d-bcf12debfa55"
    SamAccountName     = "comercial1"
    SID                = "S-1-5-21-8228041-1025387836-864803159-1605"
    Surname            = ""
    UserPrincipalName  = "comercial1@ivl.local"

````
---

## 8. Conectividad SSH y PuTTY instalados

### Conectividad SSH

**Comando**

```
ssh tecnico1@cliente03
where putty
```

**Salida**
```
salida
salida
salida
salida
salida

```
