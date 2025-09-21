# Assistente_Virtual
Sistema de assistência virtual, utilizando PLN (Processamento de Linguagem Natural), com base nas bibliotecas apresentadas durante o curso BairesDev - Machine Learning Training
Este é um projeto de **Assistente Virtual** em Python 3.13, utilizando **Vosk** para reconhecimento de voz offline e **pyttsx3** para síntese de voz (text-to-speech).

## 🚀 Funcionalidades
- Reconhecimento de fala em português (Vosk)
- Conversão de texto em voz (pyttsx3)
- Comandos por voz:
  - Pesquisar no **Wikipedia**
  - Abrir o **YouTube**
  - Mostrar **farmácias próximas** no Google Maps
  - Encerrar o assistente

## 📦 Requisitos
- Python 3.13+
- Microfone
- Conexão com a internet (para comandos que abrem sites)

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/SEU_USUARIO/assistente-virtual.git
cd assistente-virtual
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Baixe o modelo de voz em português do Vosk [aqui](https://alphacephei.com/vosk/models) e extraia na pasta do projeto.

## ▶️ Como rodar

```bash
python assistant.py
```

## 📝 Licença
Projeto para fins educacionais ainda em aperfeiçoamento.
