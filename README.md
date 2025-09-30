# GHL Appointments API

[![CI](https://github.com/Adrian-nex/GHL-Appointments-Api/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Adrian-nex/GHL-Appointments-Api/actions/workflows/ci.yml)

API de citas construida con Django y Django REST Framework.

## Requisitos

- Python 3.10 o 3.11
- Git

## Inicio rápido

Clonar y crear entorno virtual:

```bash
git clone https://github.com/Adrian-nex/GHL-Appointments-Api.git
cd GHL-Appointments-Api
python -m venv venv
.\n+venv\Scripts\Activate.ps1  # En PowerShell (Windows)
# source venv/bin/activate  # En Linux/Mac
pip install --upgrade pip
pip install -r backend/requirements.txt
```

Aplicar migraciones y ejecutar servidor de desarrollo:

```bash
cd backend
python manage.py migrate --noinput
python manage.py runserver
```

## Ejecutar tests

```bash
cd backend
python manage.py test --verbosity=2
python -m unittest discover -s . -p "test_*.py" -v
```

## Integración continua

El workflow de GitHub Actions se ejecuta en push/PR a `main`:

- Instala dependencias
- Ejecuta migraciones
- Corre la suite de tests en Python 3.10 y 3.11

Archivo del pipeline: `.github/workflows/ci.yml`.


