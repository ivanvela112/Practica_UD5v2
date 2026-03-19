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
dc01
dc02
fs01
cliente01
cliente02
cliente03
```

## 2. Estructura de ficheros en D: desde el DC1

**Comando**

```
tree \\FS01\empresa
```

**Salida**

```
empresa
comun
tecnicos
comerciales
direccion
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
OU_Tecnicos
OU_Comerciales
OU_Equipos
Administrador
adm_dominio
adm_fileserver
tecnico1
tecnico2
comercial1
comercial2
GG_Tecnicos
GG_Comerciales
Domain Admins
Domain Users
```
---

## 4. Carpetas V6 de los perfiles móviles

**Comando**

```
Get-ADUser -Filter * -Properties ProfilePath | Select Name, ProfilePath
```

**Salida**
```
tecnico1 \FS01\perfiles\tecnico1
tecnico2 \FS01\perfiles\tecnico2
comercial1 \FS01\perfiles\comercial1
comercial2 \FS01\perfiles\comercial2
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
tecnico BUILTIN\Administrators NT AUTHORITY\SYSTEM Allow FullControl
BUILTIN\Administrators Allow FullControl
EMPRESA\tecnico1 Allow Modify, Synchronize
tecnico1
tecnico2
comercial1
comercial2
usuarios
/etc/fstab
```
---

## 6. Comprobación GPOs funcionando

**Comando**

```
gpresult /r
```

**Salida**
```
Applied Group Policy Objects

Default Domain Policy
GPO_Equipos
GPO_Usuarios
```
---

## 7. Restricciones de logging

**Comando**

```
Get-ADUser comercial1 -Properties LogonHours,LogonWorkstations
```

**Salida**
```
DistinguishedName : CN=comercial1,OU=OU_Comerciales,DC=empresa,DC=local
GivenName : comercial1
Name : comercial1
ObjectClass : user
SamAccountName : comercial1
LogonHours :
LogonWorkstations : CLIENTE01,CLIENTE02
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
tecnico1@'s password:
Welcome to Ubuntu 24.04 LTS
tecnico1@cliente03:~$
C:\Program Files\PuTTY\putty.exe
```
