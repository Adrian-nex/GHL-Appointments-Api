# GHL Appointments API

[![CI](https://github.com/Adrian-nex/GHL-Appointments-Api/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Adrian-nex/GHL-Appointments-Api/actions/workflows/ci.yml)

API de citas con Django y Django REST Framework. Incluye CI en GitHub Actions y colección Postman para pruebas end-to-end.

## Estructura
```
backend/                 # Proyecto Django (API)
  appointments/          # App de citas
  mi_proyecto/           # Configuración Django
  requirements.txt       # Dependencias
docs/                    # Colecciones y guías de Postman
.github/workflows/ci.yml # Pipeline de CI
```

## Requisitos
- Python 3.10 o 3.11
- Git

## Configuración rápida
```bash
git clone https://github.com/Adrian-nex/GHL-Appointments-Api.git
cd GHL-Appointments-Api
python -m venv venv
venv\Scripts\Activate.ps1  # Windows PowerShell
# source venv/bin/activate  # Linux/Mac
pip install --upgrade pip
pip install -r backend/requirements.txt
```

Migraciones y servidor:
```bash
cd backend
python manage.py migrate --noinput
python manage.py runserver
```

## Endpoints principales
- GET `api/appointments/` — Listar citas
- POST `api/appointments/create/` — Crear cita
- PUT `api/appointments/{ghl_id}/update/` — Reprogramar
- DELETE `api/appointments/{ghl_id}/delete/` — Cancelar

## Pruebas con Postman
- Colección: `docs/GHL_API_Collection_Updated.postman_collection.json`
- Variable recomendada: `base_url = http://localhost:8000`

## Tests
```bash
cd backend
python manage.py test --verbosity=2
python -m unittest discover -s . -p "test_*.py" -v
```

## Integración continua
GitHub Actions ejecuta en push/PR a `main`:
- Instalación de dependencias y migraciones
- Tests en Python 3.10 y 3.11
- Job Postman (Newman) sobre la colección

Archivo: `.github/workflows/ci.yml`.


