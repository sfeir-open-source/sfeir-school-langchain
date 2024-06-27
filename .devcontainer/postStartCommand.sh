#!/bin/sh

# Starting Ollama Server
echo "🏃🏿‍♂️ Starting Ollama Server..."
ollama serve & 

echo "⬇️ Pulling LLMs..."
ollama pull llama2
#ollama pull mistral
#ollama pull codellama

echo "✅ Local LLMs Setup done!" 


# Activate the virtual environment for this terminal session
echo ""
echo "Please don't forget to run the following command in your terminal..."
echo "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
echo "source .school.venv/bin/activate"
echo "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
echo "...(to activate the virtual env) before installing Python dependencies!"
echo ""