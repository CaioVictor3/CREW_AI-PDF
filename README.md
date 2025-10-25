# 🛡️ Assistente de Defesa do Consumidor

Este projeto utiliza CrewAI e Streamlit para criar um assistente inteligente que responde perguntas sobre o **Código de Defesa do Consumidor (CDC)** brasileiro baseado na Lei 8.078/1990 e regulamentações relacionadas.

## 🚀 Como executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com uma das seguintes configurações:

**Opção 1: Google Gemini 2.5 Flash (recomendado)**
```
GEMINI_API_KEY=sua_chave_gemini_aqui
GEMINI_MODEL=gemini-2.0-flash-exp
```

**Opção 2: OpenAI**
```
OPENAI_API_KEY=sua_chave_openai_aqui
OPENAI_MODEL=gpt-4o-mini
```

**Como obter as chaves:**
- **Google Gemini**: Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenAI**: Acesse [OpenAI Platform](https://platform.openai.com/api-keys)

**Dica**: Use o arquivo `env.example` como modelo!

### 3. Executar o aplicativo
```bash
streamlit run streamlit_app.py
```

O aplicativo estará disponível em: http://localhost:8501

## 📁 Estrutura do projeto

- `streamlit_app.py` - Interface Streamlit principal
- `main.py` - Lógica principal do assistente
- `crew.py` - Configuração do CrewAI
- `config/` - Configurações dos agentes e tarefas
  - `agents.yaml` - Configuração do especialista em defesa do consumidor
  - `tasks.yaml` - Configuração das tarefas de resposta
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
- `file1.pdf` - Documento principal sobre Código de Defesa do Consumidor

## 🎯 Funcionalidades

- **Interface web intuitiva** em português
- **Análise de documentos PDF** sobre direitos do consumidor
- **Respostas especializadas** baseadas no CDC brasileiro
- **Suporte a múltiplos modelos de LLM** (Gemini e OpenAI)
- **Configuração flexível** de agentes e tarefas
- **Orientação prática** sobre direitos do consumidor

## 🛡️ Especialização

O assistente é especializado em:
- **Código de Defesa do Consumidor (Lei 8.078/1990)**
- **Direitos básicos do consumidor**
- **Responsabilidade do fornecedor**
- **Práticas comerciais**
- **Contratos de consumo**
- **Mecanismos de defesa**

## ⚠️ Notas importantes

- Certifique-se de ter uma chave de API válida configurada
- Os documentos PDF devem estar na pasta `knowledge/`
- O primeiro uso pode demorar um pouco para processar os documentos
- O assistente fornece orientações gerais e não substitui consultoria jurídica profissional

## 🔍 Exemplos de uso

- "Quais são os direitos básicos do consumidor?"
- "Como proceder quando um produto apresenta defeito?"
- "O que fazer se o fornecedor não cumpre o prazo de entrega?"
- "Quais são as práticas comerciais abusivas?"
- "Como funciona a responsabilidade do fornecedor por vícios do produto?"