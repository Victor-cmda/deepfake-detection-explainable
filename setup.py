# setup_project.py
import os
import subprocess
import sys
import argparse
from pathlib import Path

def create_directory_structure():
    """Cria a estrutura de diretórios do projeto"""
    directories = [
        "data/raw",
        "data/processed",
        "data/models",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "src/utils",
        "src/evaluation",
        "src/config",
        "tests",
        "app",
        "docs",
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # Criar arquivo __init__.py em cada diretório Python
        if directory.startswith("src") or directory == "tests":
            init_file = Path(directory) / "__init__.py"
            init_file.touch(exist_ok=True)
    
    print("✓ Estrutura de diretórios criada")