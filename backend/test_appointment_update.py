#!/usr/bin/env python
"""
Script de prueba para verificar la actualización de citas
"""
import os
import sys
import django
import requests
import json
from datetime import datetime, timedelta

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from appointments.models import Appointment

def test_appointment_update():
    """Prueba la actualización de una cita"""
    
    # URL base del servidor
    base_url = "http://localhost:8000"
    
    # Datos de prueba
    test_data = {
        "title": "Cita Reprogramada - Test",
        "startTime": "2025-10-03T14:00:00-05:00",
        "endTime": "2025-10-03T15:00:00-05:00"
    }
    
    print("=== Prueba de Actualización de Cita ===")
    print(f"Datos de prueba: {json.dumps(test_data, indent=2)}")
    
    # Buscar una cita existente en la BD
    appointment = Appointment.objects.first()
    if not appointment:
        print("❌ No se encontraron citas en la base de datos")
        print("   Primero crea una cita usando el endpoint de creación")
        return False
    
    print(f"✅ Cita encontrada: {appointment.title} (ID: {appointment.ghl_id})")
    
    # URL de actualización
    update_url = f"{base_url}/api/appointments/{appointment.ghl_id}/update/"
    print(f"URL de actualización: {update_url}")
    
    try:
        # Realizar la petición PUT
        response = requests.put(
            update_url,
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Actualización exitosa")
            return True
        else:
            print("❌ Error en la actualización")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    success = test_appointment_update()
    sys.exit(0 if success else 1)
