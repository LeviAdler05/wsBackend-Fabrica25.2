# setup.ps1 - Script de Instalação do Projeto Anime

# Exibe uma mensagem de boas-vindas
Write-Host "🚀 Iniciando a instalação do Projeto Anime..." -ForegroundColor Green

# Passo 1: Constrói e inicia os containers Docker em segundo plano
Write-Host "🏗️  Passo 1 de 3: Construindo e iniciando os containers (Isso pode levar alguns minutos na primeira vez)..."
docker-compose up --build -d

# Verifica se o docker-compose foi executado com sucesso
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro ao executar 'docker-compose up'. Verifique a instalação do Docker e tente novamente." -ForegroundColor Red
    exit
}

Write-Host "✅ Containers iniciados com sucesso!" -ForegroundColor Green

# Adiciona uma pausa para garantir que o banco de dados esteja pronto
Write-Host "⏳ Aguardando 15 segundos para o banco de dados iniciar completamente..."
Start-Sleep -Seconds 15

# Passo 2: Popula o banco de dados com os animes
Write-Host "📚 Passo 2 de 3: Populando o banco de dados com animes..."
docker-compose exec web python manage.py import_animes

Write-Host "✅ Banco de dados populado!" -ForegroundColor Green

# Passo 3: Instruções para o usuário criar sua conta
Write-Host "👤 Passo 3 de 3: Crie sua conta de administrador!" -ForegroundColor Yellow
Write-Host "A aplicação está no ar em http://localhost:8000"
Write-Host "Agora, execute o seguinte comando NESTE terminal para criar seu usuário e senha:" -ForegroundColor Cyan
Write-Host ""
Write-Host "   docker-compose exec web python manage.py createsuperuser" -ForegroundColor White
Write-Host ""

Write-Host "🎉 Instalação finalizada! Após criar seu usuário, aproveite o projeto." -ForegroundColor Green
