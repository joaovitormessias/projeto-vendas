# 🤖 Projeto: Inteligência Artificial para Análise de Dados na Zoop

## 📌 Sobre o Projeto

Fomos contratados pela **Zoop**, uma rede de lojas de varejo, para desenvolver uma **inteligência artificial generativa** capaz de automatizar o processo de análise de dados. O objetivo é **acelerar a tomada de decisão** e permitir uma gestão mais **rápida e eficiente**.

O sistema deve possibilitar que o time de dados realize consultas **em linguagem natural**, como por exemplo:

> "Qual foi o faturamento de vendas no mês anterior?"

A IA interpretará a pergunta e responderá com base nos dados fornecidos, garantindo uma análise precisa e segura.

---

## 🛠 Etapas da Implementação

1. **Desafios Enfrentados** ⚠️
   - Dependência de análises manuais, que são demoradas e podem gerar gargalos.
   - Necessidade de proteger os dados sensíveis da empresa, evitando dependência de modelos externos.

2. **Solução Proposta** 🚀
   - Desenvolver um modelo baseado no **LlamaIndex**, que integra um **Large Language Model (LLM)** diretamente aos dados da Zoop.
   - Garantir **segurança** e **privacidade**, sem compartilhar informações confidenciais com terceiros.
   - Permitir consultas intuitivas e interativas, eliminando a necessidade de análise manual.

---

## 🔧 Configuração do Ambiente

### 🔹 Requisitos

- **Python 3.9+**
- **Anaconda** (recomendado) ou **Jupyter Notebook**

### 🔹 Instalação do Ambiente

1. Baixe e instale o [Anaconda](https://www.anaconda.com/products/distribution).
2. Crie um novo ambiente virtual:
   ```sh
   conda create -n zoop_ai python=3.9
   ```
3. Ative o ambiente:
   ```sh
   conda activate zoop_ai
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

### 🔹 Executando o Projeto

1. Suba a aplicação Gradio:
   ```sh
   python app.py
   ```
2. Acesse a interface no navegador e faça consultas interativas.

---

## 📚 Tecnologias Utilizadas

- **LlamaIndex** → Integração de LLM com dados tabulares
- **Groq API** → Processamento de linguagem natural
- **Gradio** → Interface interativa
- **Pandas** → Manipulação de dados
- **FPDF** → Geração de relatórios em PDF

---

## 🤝 Contribuição

Se deseja contribuir para o projeto, siga os passos:

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b minha-melhoria`
3. Realize suas alterações e commit: `git commit -m 'Melhoria na IA'`
4. Envie suas mudanças: `git push origin minha-melhoria`
5. Abra um Pull Request.

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - consulte o arquivo `LICENSE` para mais detalhes.

---

🚀 *Desenvolvido como parte do projeto de automação de análise de dados para a Zoop.*

