# Microservicio de Gráficas
### Introducción

Este microservicio se encarga de generar gráficas basadas en los datos de otros microservicios de una aplicación para la gestión académica de una universidad. Los gráficos incluyen, entre otros, análisis de rendimiento académico, necesidades especiales de educación, y estadísticas relacionadas con los cursos. Estos gráficos son orientados a cada uno de los posibles usuarios que puede tener nuestra aplicación (en este caso admin/director, profesores y estudiantes).

### Requisitos previos

Antes de ejecutar el microservicio, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.8+**    
- **Flask**: Framework para el desarrollo de aplicaciones web en Python.
- Otros microservicios (usuarios, cursos, etc.) en funcionamiento.
    
    https://github.com/natam226/proyecto_curso_redes
    

### Dependencias

El proyecto requiere ciertas bibliotecas de Python que deben ser instaladas. Puedes hacerlo mediante un archivo `requirements.txt` que contiene todas las dependencias necesarias.

Archivo `requirements.txt` (En caso de querer añadirlo):

```
flask
requests
plotly
pandas
Flask_cors
```

Para instalar las dependencias, ejecuta:

```bash
python3 -m pip install flask requests pandas plotly Flask_cors --no-warn-script-location
```

### Estructura del proyecto

La estructura de carpetas y archivos del microservicio es la siguiente:

```
graficas/
├── src/
│   ├── app.py                   # Archivo principal para ejecutar la aplicación
│   ├── controllers/             # Contiene la lógica de los endpoints
│   │   ├── estudianteController.py
│   │   ├── profesorController.py
│   │   └── administradorController.py
│   ├── models/                  # Contiene la lógica para acceder a los datos
│   │   ├── estudiantesModel.py
│   │   ├── cursosModel.py
│   │   └── profesoresModel.py
│   ├── services/                # Contiene la lógica para generar los gráficos
│       ├── graficoService.py 
└── README.md                    # Documentación del proyecto

```

### Configuración (actualizar)

1. **Configurar endpoints para generación de las graficas:**
    - Estas URLs son los endpoints donde están alojados los otros microservicios.
        
        Endpoints necesarios para el desarrollo de las graficas (Cambiar URLs según sea necesario)
        
        **En profesoresModel.py**
        
        - Para la función `obtener_correo_profesor`:  http://localhost:3005/correoprof/{*usuario*}
        
        **En estudiantesModel.py**
        
        - Para la función `obtener_correo_estudiante`: http://localhost:3005/CorreoEstudiante/{*usuario*}
        - Para la función `obtener_informacion_estudiante`: http://localhost:3005/estudiantes
        
        **En cursosModel.py**
        
        - Para la función `obtener_rendimiento_estudiantes`: http://localhost:3007/cursos/rendimiento/{*correoProf*}
        - Para la función `obtener_notas_estudiante`: http://localhost:3007/cursos/notas/{*correoEstudiante*}
        - Para la función `obtener_notas_estudiantes`: http://localhost:3007/cursos
2. **Instalación de dependencias:**
    - Ejecuta `pip install flask requests pandas plotly Flask_cors` para instalar las dependencias.

### Cómo ejecutar el microservicio

Para ejecutar el microservicio, sigue estos pasos:

1. Dirígete a la carpeta `graficas/` y ejecuta el siguiente comando:
    
    ```bash
    python src/app.py
    
    ```
    
2. Accede a los endpoints a través de `http://localhost:3008/<ruta-endpoint>`.

### Endpoints disponibles

1. **Gráfica del promedio por estudiante:**
    - **Ruta:** `http://localhost:3008/estudiante/<usuario>/grafico-promedio`
    - **Método:** `GET`
    - **Descripción:** Genera un gráfico del promedio acumulado de un estudiante.
2. **Gráfica de aprobados y reprobados por materia (para profesores):**
    - **Ruta:** `http://localhost:3008/profesor/<usuario>/grafico-aprobados-reprobados`
    - **Método:** `GET`
    - **Descripción:** Muestra una gráfica de barras que representa la cantidad de estudiantes aprobados y reprobados en cada materia.
3. **Gráfica de estado civil vs promedio de los estudiantes(para administrador):**
    - **Ruta:** `http://localhost:3008/admin/grafico-estadoCivil`
    - **Método:** `GET`
    - **Descripción:** Muestra una grafica de violines de estado civil vs promedio acumulado de los estudiantes.
4. **Gráfica de préstamo vs promedio de los estudiantes(para administrador):**
    - **Ruta:** `http://localhost:3008/admin/grafico-prestamo`
    - **Método:** `GET`
    - **Descripción:** Muestra una grafica de violines de préstamo vs promedio acumulado de los estudiantes.
5. **Gráfica de beca vs promedio de los estudiantes(para administrador):**
    - **Ruta:** `http://localhost:3008/admin/grafico-beca`
    - **Método:** `GET`
    - **Descripción:** Muestra una grafica de violines de beca vs promedio acumulado de los estudiantes.
6. **Gráfica de desplazado vs promedio de los estudiantes(para administrador):**
    - **Ruta:** `http://localhost:3008/admin/grafico-desplazado`
    - **Método:** `GET`
    - **Descripción:** Muestra una grafica de violines de desplazado vs promedio acumulado de los estudiantes.
7. **Gráfica de necesidades especiales de educación vs promedio de los estudiantes(para administrador):**
    - **Ruta:** `http://localhost:3008/admin/grafico-necesidades`
    - **Método:** `GET`
    - **Descripción:** Muestra una gráfica de violines de necesidades especiales de educación vs promedio acumulado de los estudiantes.

### Ejemplos de uso

### Usando `curl`:

```bash
curl <http://localhost:3008/estudiante/john_doe/grafico-promedio>

```

### Solución de problemas

- **Problemas con la instalación de dependencias**
    - Si recibes un error de instalación, verifica que estás usando la versión correcta de Python y que `pip` está actualizado.

### Consideraciones

1. **Integración con otros microservicios**: Asegúrate de que los microservicios de usuarios, cursos y asignaturas estén corriendo correctamente.
