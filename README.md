# 🖥️ Práctica – Comprobaciones del dominio (Active Directory)

## 🎯 Objetivo

El objetivo de esta práctica es comprobar que la infraestructura de dominio funciona correctamente:

* Equipos en el dominio
* Estructura de carpetas
* Usuarios, grupos y OU
* Perfiles móviles
* Permisos NTFS y comparticiones
* GPOs
* Restricciones de login
* Conectividad Linux (SSH + SAMBA)

---

## 📦 Entrega

La entrega se realiza en el archivo:

```
entrega/respuesta.md
```

⚠️ **Muy importante:**

* No modificar la estructura del documento
* Solo rellenar las salidas de los comandos
* Copiar y pegar la salida real (NO escribirla a mano)

---

## 📝 Cómo completar la práctica

Cada ejercicio tiene este formato:

```
**Comando**
```

comando

```

**Salida**
```

resultado

```
```

### Ejemplo

```
**Comando**
```

Get-ADComputer -Filter * | Select Name,OperatingSystem

```

**Salida**
```

Almendro
Antonio
Manolo

```
```

---

## ⚠️ Errores comunes

❌ No usar ```
❌ Escribir la salida a mano
❌ Modificar el formato del documento

---


## 🚀 Flujo completo

```
Alumno → edita respuesta.md
        ↓
GitHub → detecta cambios
        ↓
Actions → ejecuta corregir.py
        ↓
Script → compara con reglas.yaml
        ↓
Resultado → feedback.md
```

---


## 👨‍🏫 Nota del profesor

Este sistema simula un entorno real de trabajo:

* entrega automatizada
* validación objetiva
* feedback inmediato

---

## 🏁 Resultado esperado

Una entrega correcta debe:

✔ tener todos los bloques completados
✔ coincidir con la estructura del dominio
✔ cumplir las comprobaciones técnicas

---

**¡Buena suerte! 🚀**
