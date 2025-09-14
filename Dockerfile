FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . /app/

# Copia o entrypoint script
COPY entrypoint.sh /app/

# Torna o entrypoint executável
RUN chmod +x /app/entrypoint.sh

# Expõe a porta que o container vai usar
EXPOSE 8000

# Define o entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]