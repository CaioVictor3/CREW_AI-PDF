# Assistente de Compliance Farmacêutico

Este projeto utiliza CrewAI e Streamlit para criar um assistente inteligente que responde perguntas sobre compliance regulatório farmacêutico baseado em documentos da ANVISA.

## 🚀 Como executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com uma das seguintes configurações:

**Opção 1: Google Gemini (recomendado)**
```
GEMINI_API_KEY=sua_chave_gemini_aqui
GEMINI_MODEL=gemini-1.5
```

**Opção 2: OpenAI**
```
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_MODEL=gpt-4o-mini
```

### 3. Executar o aplicativo
```bash
streamlit run app.py
```

O aplicativo estará disponível em: http://localhost:8501

## 📁 Estrutura do projeto

- `app.py` - Interface Streamlit principal
- `main.py` - Lógica principal do assistente
- `crey.py` - Configuração do CrewAI
- `config/` - Configurações dos agentes e tarefas
- `knowledge/` - Documentos PDF para análise

## 🔧 Configuração

### Obter chaves de API

**Google Gemini:**
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova chave de API
3. Adicione no arquivo `.env`

**OpenAI:**
1. Acesse [OpenAI Platform](https://platform.openai.com/api-keys)
2. Crie uma nova chave de API
3. Adicione no arquivo `.env`

## 📚 Documentos suportados

O assistente analisa automaticamente os seguintes documentos na pasta `knowledge/`:
- `file.pdf`
- `rdc0044_17_08_2009.pdf`
- `tema-7-21.pdf`

## 🎯 Funcionalidades

- Interface web intuitiva
- Análise de documentos PDF
- Respostas baseadas em conhecimento específico
- Suporte a múltiplos modelos de LLM
- Configuração flexível de agentes

## ⚠️ Notas importantes

- Certifique-se de ter uma chave de API válida configurada
- Os documentos PDF devem estar na pasta `knowledge/`
- O primeiro uso pode demorar um pouco para processar os documentos
