# Backend - GHL Appointments API

Este directorio contiene el proyecto Django (API REST) para gestionar citas al estilo GoHighLevel.

## Requisitos
- Python 3.10 o 3.11

## Instalación
```bash
python -m venv venv
venv\Scripts\Activate.ps1  # Windows PowerShell
# source venv/bin/activate  # Linux/Mac
pip install --upgrade pip
pip install -r requirements.txt
```

## Variables de entorno
Crea un archivo `.env` (puedes usar `backend/.env.example` como referencia) y define, según corresponda:
- `DEBUG=true`
- `SECRET_KEY=tu_secret_key`
- `ALLOWED_HOSTS=127.0.0.1,localhost`
- `GHL_ACCESS_TOKEN=tu_access_token`

## Migraciones y servidor
```bash
python manage.py migrate --noinput
python manage.py runserver
```

Servidor por defecto: `http://127.0.0.1:8000/`

## Endpoints principales
- GET `/api/appointments/` — Listar citas
- POST `/api/appointments/create/` — Crear cita
- PUT `/api/appointments/{ghl_id}/update/` — Reprogramar
- DELETE `/api/appointments/{ghl_id}/delete/` — Cancelar

## Tests
```bash
python manage.py test --verbosity=2
python -m unittest discover -s . -p "test_*.py" -v
```

## Postman
La colección actualizada está en `../docs/GHL_API_Collection_Updated.postman_collection.json`.
Usa `base_url = http://127.0.0.1:8000`.


