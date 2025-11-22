#!/usr/bin/env bash

# Função para instalação básica
setup_basic() {
    echo "Instalando ferramentas básicas..."
    pipx install tko
    code --install-extension usernamehw.errorlens
    code --install-extension bierner.markdown-preview-github-styles
    echo "✓ Ferramentas básicas instaladas"
}

# Função para configuração Python
setup_python() {
    echo ""
    echo "Configurando ambiente Python..."
    mkdir -p .vscode
    cat > .vscode/settings.json <<EOF
{
    "python.analysis.typeCheckingMode": "strict",
    "python.analysis.diagnosticMode": "workspace"
}
EOF
    code --install-extension ms-python.python
    echo "✓ Ambiente Python configurado"
}

# Função para configuração TypeScript
setup_typescript() {
    echo ""
    echo "Configurando ambiente TypeScript..."
    npm install -g typescript esbuild
    cd /workspaces
    npm install --save-dev @types/node readline-sync
    echo "✓ Ambiente TypeScript configurado"
}

# Início do script
echo "========================================"
echo "   Setup de Ambiente de Desenvolvimento"
echo "========================================"
echo ""

# Configuração básica (sempre executada)
setup_basic
echo ""

# Menu de opções
echo "Escolha o tipo de projeto que deseja configurar:"
echo "1) Python"
echo "2) TypeScript"
echo "3) Ambos (Python + TypeScript)"
echo "4) Nenhum (apenas configuração básica)"
echo ""
read -p "Digite sua escolha [1-4]: " choice

case $choice in
    1)
        setup_python
        ;;
    2)
        setup_typescript
        ;;
    3)
        setup_python
        setup_typescript
        ;;
    4)
        echo ""
        echo "Configuração básica concluída. Nenhum ambiente adicional foi configurado."
        ;;
    *)
        echo ""
        echo "Opção inválida. Apenas a configuração básica foi aplicada."
        ;;
esac

echo ""
echo "========================================"
echo "   Setup concluído!"
echo "========================================"