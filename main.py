"""
Sistema Impacto Climático — Ponto de entrada principal
"""
import os
import sys
import subprocess

def verificar_dados():
    """Verifica se os dados existem, gera se necessário."""
    base = os.path.dirname(os.path.abspath(__file__))
    arquivos = ["chuva.csv", "desastres.csv", "eventos_combinados.csv"]
    faltando = [f for f in arquivos if not os.path.exists(os.path.join(base, "data", f))]
    
    if faltando:
        print("📦 Dados não encontrados. Gerando dados de demonstração...")
        subprocess.run([sys.executable, os.path.join(base, "gerar_dados.py")], check=True)
        print("✅ Dados gerados com sucesso!\n")
    else:
        print("✅ Dados encontrados em ./data/\n")

def iniciar_dashboard():
    """Inicia o dashboard Streamlit."""
    base = os.path.dirname(os.path.abspath(__file__))
    dashboard_path = os.path.join(base, "dashboard.py")
    
    print("🚀 Iniciando Sistema Impacto Climático...")
    print("=" * 50)
    print("🌧️  Dashboard: http://localhost:8501")
    print("   Pressione Ctrl+C para encerrar")
    print("=" * 50)
    
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", dashboard_path,
        "--server.port", "8501",
        "--server.headless", "false",
        "--theme.base", "dark",
    ])

if __name__ == "__main__":
    verificar_dados()
    iniciar_dashboard()
