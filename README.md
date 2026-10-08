# Evaluación Sumativa 2 - Desarrollo Back End con Django

## 👥 Integrantes del Proyecto
- **Alumno:** Reinaldo Opaso
- **Asignatura:** Back End (6to Semestre)
- **Repositorio:** [https://github.com/Bell-091/----evaluacion-2.git](https://github.com/Bell-091/----evaluacion-2.git)

---

## 📌 Descripción del Proyecto
Aplicación web desarrollada en **Django** con arquitectura **MVT** (*Model - View - Template*), estructurada con namespaces de URLs, componentes dinámicos de **Bootstrap 5** y manejo de archivos estáticos. 

El proyecto cuenta con un catálogo categorizado por géneros cinematográficos (**Acción y Aventura** y **Ciencia Ficción y Espacio**), donde cada uno dispone de al menos **10 películas completas** con imágenes, año de estreno, director, puntuación IMDb, badges y modales de detalles interactivos.

---

## 🛠️ Requisitos e Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/Bell-091/----evaluacion-2.git
cd ----evaluacion-2
```

### 2. Crear y activar el entorno virtual
En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

Abrir en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🌿 Flujo de Trabajo con Git y Ramas

Para el trabajo colaborativo se implementaron 2 ramas de trabajo:
- `feature-alumno1` / `feature-reinaldo`: Desarrollo de la estructura base, configuración del proyecto Django, vistas principales y archivos estáticos.
- `feature-alumno2` / `feature-catalogo`: Implementación de los templates de catálogo, modales de Bootstrap, filtros y formulario de contacto.
- `main`: Rama principal donde se integran todos los cambios validados.

### Comandos Git utilizados:
```bash
# Crear y cambiar a rama de trabajo
git checkout -b feature-reinaldo

# Guardar cambios
git add .
git commit -m "feat(templates): se implementa catalogo de peliculas con modales y bootstrap 5"

# Subir rama
git push -u origin feature-reinaldo

# Integrar a main
git checkout main
git merge feature-reinaldo
git push origin main
```

---

## 📂 Estructura del Proyecto

```
Desarrolloevaluacion2/
│── manage.py
│── requirements.txt
│── .gitignore
│── README.md
│── reinaldo_opaso/                     # Configuración principal del proyecto
│   │── __init__.py
│   │── settings.py                    # Configuración de apps, templates y static
│   │── urls.py                        # Enrutador principal con namespace 'home'
│   │── wsgi.py
│   └── asgi.py
│── home_reinaldo_opaso/                # Aplicación Django 'home'
│   │── migrations/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── views.py                       # Vistas y dataset de géneros/películas
│   └── urls.py                        # URLs internas de la app
│── static/                            # Archivos estáticos
│   │── css/
│   │   └── estilos.css                # Estilos personalizados y tema oscuro
│   └── js/
│       └── main.js                    # Scripts de interactividad
└── templates/                         # Plantillas HTML
    └── home_app/
        │── base.html                  # Plantilla base con Navbar y Footer
        │── inicio.html                # Bienvenida y tarjetas de géneros
        │── peliculas.html             # Catálogo de 10 películas por género
        └── contacto.html              # Formulario con método POST y CSRF
```
