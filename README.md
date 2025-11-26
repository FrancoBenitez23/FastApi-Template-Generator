# FastAPI Project Template Creator

Script de Python para crear automáticamente una estructura de proyecto FastAPI completa con gestión de dependencias y entorno virtual.

## Características

- 🏗️ Creación automática de estructura de archivos y carpetas
- 🐍 Creación automática de entorno virtual
- 📦 Gestor interactivo de `requirements.txt`
- 🎯 CLI intuitiva con menú de opciones
- ✨ Archivos vacíos listos para desarrollar
- 📁 Estructura jerárquica organizada (`app/` y `venv/` separados)

## Estructura del Proyecto

El script crea la siguiente estructura jerárquica:

```
tu_proyecto/
├── app/                          # Código de la aplicación
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   └── schemas.py
│   │   └── posts/
│   │       ├── repository.py
│   │       ├── router.py
│   │       └── schemas.py
│   ├── core/
│   │   ├── db.py
│   │   └── security.py
│   └── models/
│       └── __init__.py
├── venv/                         # Entorno virtual (opción 3 o 4)
│   ├── bin/ (Linux/Mac) o Scripts/ (Windows)
│   ├── lib/
│   └── ...
└── requirements.txt              # Dependencias del proyecto
```

## 🏛️ Arquitectura: Patrón DTO (Data Transfer Objects)

Este proyecto sigue una arquitectura basada en **DTOs** usando Pydantic, separando claramente las capas:

### Capas de la Arquitectura

```
Cliente HTTP
    ↓
Router (api/*/router.py)           → Define endpoints
    ↓
Repository (api/*/repository.py)   → Lógica de negocio y acceso a datos
    ↓
Models (models/*.py)               → Entidades de base de datos (ORM)
    ↓
Base de Datos
```


## Uso

### Ejecutar el script

```bash
python create_structure.py
```

### Menú Principal

El script presenta 5 opciones:

```
==================================================
  FastAPI Project Template Creator
==================================================

1. Create project structure
2. Manage requirements.txt
3. Full setup (structure + venv + requirements)
4. Create virtual environment only
5. Exit

Select an option (1-5):
```

#### Opción 1: Create project structure
Crea únicamente la estructura de archivos y carpetas vacías dentro de `app/`.

#### Opción 2: Manage requirements.txt
Gestor interactivo para crear/actualizar el archivo `requirements.txt`:
- Muestra paquetes existentes si el archivo ya existe
- Permite agregar paquetes uno por uno
- Acepta versiones específicas (ej: `fastapi==0.104.1`)
- Evita duplicados automáticamente
- Escribe `skip` para saltar este paso
- Presiona Enter en vacío para finalizar

**Ejemplo de uso:**
```
Package name (with optional version, e.g., 'fastapi==0.104.1'): fastapi
  ✓ Added: fastapi
Package name (with optional version, e.g., 'fastapi==0.104.1'): uvicorn[standard]
  ✓ Added: uvicorn[standard]
Package name (with optional version, e.g., 'fastapi==0.104.1'): sqlalchemy==2.0.23
  ✓ Added: sqlalchemy==2.0.23
Package name (with optional version, e.g., 'fastapi==0.104.1'):

✓ Created/Updated requirements.txt
  Total packages: 3
```

#### Opción 3: Full setup ⭐ (Recomendado)
Ejecuta el setup completo del proyecto:
1. Crea la estructura en `app/`
2. Crea el entorno virtual en `venv/`
3. Gestiona `requirements.txt`

Esta es la opción más completa y deja tu proyecto listo para empezar a trabajar.

#### Opción 4: Create virtual environment only
Crea únicamente el entorno virtual en `venv/`. Útil si ya tienes la estructura creada.

#### Opción 5: Exit
Cierra el programa.

## Instalación de Dependencias

### Con la opción 3 (Full setup) - Automático ⚡

Si usaste la opción 3, el entorno virtual ya está creado. Solo necesitas:

**1. Activar el entorno virtual:**

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

**2. Instalar las dependencias:**
```bash
pip install -r requirements.txt
```

### Instalación Manual

Si no usaste la opción 3, sigue estos pasos:

**1. Crear un entorno virtual:**
```bash
python -m venv venv
```

**2. Activar el entorno virtual:**

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

**3. Instalar las dependencias:**
```bash
pip install -r requirements.txt
```

## Requisitos

- Python 3.7+
- No requiere dependencias externas

## Licencia

Libre de usar y modificar según tus necesidades.
