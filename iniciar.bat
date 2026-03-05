@echo off
chcp 65001 >nul
title Sistema Impacto Climatico

echo.
echo  ==========================================
echo   SISTEMA IMPACTO CLIMATICO
echo   Analise de Chuvas e Desastres - Brasil
echo  ==========================================
echo.

:: Verifica se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERRO] Python nao encontrado.
    echo  Instale o Python em: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

:: Vai para a pasta onde o .bat esta localizado
cd /d "%~dp0"

:: Instala dependencias se necessario
echo  Verificando dependencias...
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo  Instalando dependencias pela primeira vez...
    echo  Aguarde, isso pode levar alguns minutos.
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo  [ERRO] Falha ao instalar dependencias.
        echo  Tente executar manualmente: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
    echo.
    echo  Dependencias instaladas com sucesso!
    echo.
)

:: Gera os dados se nao existirem
if not exist "data\chuva.csv" (
    echo  Gerando dados de demonstracao...
    python gerar_dados.py
    echo.
)

:: Abre o navegador apos 3 segundos
echo  Iniciando dashboard...
echo  Acesse: http://localhost:8501
echo.
echo  Pressione Ctrl+C nesta janela para encerrar o sistema.
echo.

start "" /b timeout /t 3 /nobreak >nul & start "" "http://localhost:8501"

:: Inicia o Streamlit
python -m streamlit run dashboard.py --server.port 8501 --server.headless false --theme.base dark --browser.gatherUsageStats false

echo.
echo  Sistema encerrado.
pause
