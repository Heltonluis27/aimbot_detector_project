
@echo off
echo Verificando se o Python está instalado...

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python não encontrado. Por favor, instale o Python 3.x e marque a opção "Add Python to PATH".
    pause
    exit /b
)

echo Python encontrado. Instalando dependências...
python install_dependencies.py

echo.
echo Instalação concluída.
pause
