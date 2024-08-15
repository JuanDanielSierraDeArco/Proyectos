# Usa la imagen oficial de Python 3.12 como base
FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt a la ruta /app dentro de la imagen
COPY requirements.txt /app/requirements.txt

# Instala las dependencias listadas en requirements.txt sin usar la caché de pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Especifica el comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
