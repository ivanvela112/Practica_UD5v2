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
salida
salida
salida
salida
salida
```

## 2. Estructura de ficheros en D: desde el DC1

**Comando**

```
tree \\FS01\empresa
```

**Salida**

```
salida
salida
salida
salida
salida

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
salida
salida
salida
salida
salida
salida

```
---

## 4. Carpetas V6 de los perfiles móviles

**Comando**

```
Get-ADUser -Filter * -Properties ProfilePath | Select Name, ProfilePath
```

**Salida**
```
salida
salida
salida
salida
salida
salida

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
salida
salida
salida
salida
salida
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
salida
salida
salida
salida
salida

```
---

## 7. Restricciones de logging

**Comando**

```
Get-ADUser comercial1 -Properties LogonHours,LogonWorkstations
```

**Salida**
```
salida
salida
salida
salida
salida

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
