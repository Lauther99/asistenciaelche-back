FROM python:3.11.5

# Evitar input interactivo
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias del sistema necesarias para dlib y opencv
RUN apt-get update && apt-get install -y \
    build-essential \
    # cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto por el que uvicorn va a correr
EXPOSE 8080

# Comando de arranque
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

# docker run --env JWT_SECRET_KEY=mi_secreto_firme --env JWT_ALGORITHM=HS256 app-backend