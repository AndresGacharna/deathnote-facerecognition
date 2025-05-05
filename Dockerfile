# Usamos una imagen base que tiene Python y pip preinstalados
FROM python:3.10

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . /app/
#Backend Developed by Andrés Gacharná

# Comando para correr la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

