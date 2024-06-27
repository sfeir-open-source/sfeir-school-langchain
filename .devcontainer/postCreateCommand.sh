#!/bin/sh

# Installing Node Modules
#npm ci

# Installing Ollama

echo "⬇️ Downloading and Installing Ollama Server..."
curl https://ollama.ai/install.sh | sh

# Create the virtual environment (if missing)
if [ ! -f .school.venv/bin/activate ]; then
    echo "➕ Creating the virtual environment (.school.venv)..."
    virtualenv .school.venv
fi

echo "✅ Setup done" 

# Activate the virtual environment for this terminal session
echo ""
echo "Please don't forget to run the following command in your terminal..."
echo "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
echo "source .school.venv/bin/activate"
echo "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
echo "...(to activate the virtual env) before installing Python dependencies!"
echo ""