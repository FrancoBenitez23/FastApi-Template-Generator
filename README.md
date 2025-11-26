# FastAPI Project Template Creator

Python script to automatically create a complete FastAPI project structure with dependency management and a virtual environment.

## Features

- 🏗️ Automatic creation of file and folder structure
- 🐍 Automatic creation of virtual environment
- 📦 Interactive `requirements.txt` manager
- 🎯 Intuitive CLI with options menu
- ✨ Empty files ready for development
- 📁 Organized hierarchical structure (`app/` and `venv/` separate)

## Project Structure

The script creates the following hierarchical structure:

```
your_project/
├── app/ # Application code
│ ├── __init__.py
│ ├── main.py
│ ├── api/
│ │ ├── auth/
│ │ │ ├── router.py
│ │ │ └── schemas.py
│ │ └── posts/
│ │ ├── repository.py
│ │ ├── router.py
│ │ └── schemas.py
│ ├── core/
│ │ ├── db.py
│ │ └── security.py
│ └── models/
│ └── __init__.py
├── venv/ # Virtual environment (option 3 or 4)
│ ├── bin/ (Linux/Mac) or Scripts/ (Windows)
│ ├── lib/
│ └── ...
└── requirements.txt # Project Dependencies
```

## 🏛️ Architecture: DTO (Data Transfer Object) Pattern

This project follows a **DTO**-based architecture using Pydantic, clearly separating the layers:

### Architecture Layers

```
HTTP Client

↓
Router (api/*/router.py) → Defines endpoints

↓
Repository (api/*/repository.py) → Business logic and data access

↓
Models (models/*.py) → Entities database (ORM) 
↓
Database
```


## Use

### Run the script

```bash
python create_structure.py
```

### Main Menu

The script presents 5 options:

```
================================================================== 
FastAPI Project Template Creator
==================================================================

1. Create project structure
2. Manage requirements.txt
3. Full setup (structure + venv + requirements)
4. Create virtual environment only
5.Exit

Select an option (1-5):
```

#### Option 1: Create project structure
Creates only the empty file and folder structure within `app/`.


#### Option 2: Manage requirements.txt
Interactive manager to create/update the `requirements.txt` file:
- Displays existing packages if the file already exists
- Allows adding packages one by one
- Accepts specific versions (e.g., `fastapi==0.104.1`)
- Automatically avoids duplicates
- Type `skip` to skip this step
- Press Enter to finish

**Example of use:**
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

#### Option 3: Full setup ⭐ (Recommended)
Run the complete project setup:
1. Create the structure in `app/`
2. Create the virtual environment in `venv/`
3. Manage `requirements.txt`

This is the most complete option and leaves your project ready to start working.

#### Option 4: Create virtual environment only
Creates only the virtual environment in `venv/`. Useful if you already have the structure created.

#### Option 5: Exit
Closes the program.

## Installing Dependencies

### With Option 3 (Full setup) - Automatic ⚡

If you used option 3, the virtual environment is already created. You only need to:

**1. Activate the virtual environment:**

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

**2. Install the dependencies:**
```bash
pip install -r requirements.txt
```

### Manual Installation

If you did not use option 3, follow these steps:

**1. Create a virtual environment:**
```bash
python -m venv venv
```

**2. Activate the virtual environment:

Linux/Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.7+
- No external dependencies required

## License

Free to use and modify as needed.
