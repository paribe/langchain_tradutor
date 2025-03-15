# 🌐 Tradutor com Mistral AI

Um aplicativo de tradução de textos baseado em inteligência artificial, utilizando a API da Mistral AI e o framework LangChain.

## 📋 Descrição

Este aplicativo permite traduzir textos para múltiplos idiomas usando o modelo de linguagem avançado da Mistral AI. Desenvolvido com Streamlit para fornecer uma interface web amigável e intuitiva.

## ✨ Funcionalidades

- Tradução de textos para diversos idiomas (Inglês, Espanhol, Francês, Alemão, Italiano, etc.)
- Suporte para idiomas personalizados
- Interface intuitiva com visualização lado a lado do texto original e traduzido
- Feedback visual durante o processo de tradução

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem de programação
- [Streamlit](https://streamlit.io/) - Framework para desenvolvimento de aplicações web
- [Mistral AI](https://mistral.ai/) - API de inteligência artificial para processamento de linguagem natural
- [LangChain](https://www.langchain.com/) - Framework para desenvolvimento de aplicações baseadas em LLMs
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Gerenciamento de variáveis de ambiente

## 🚀 Instalação e Uso

### Pré-requisitos

- Python 3.9 ou superior (evite a versão 3.9.7 que possui incompatibilidades com Streamlit)
- Poetry (gerenciador de dependências)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/paribe/tradutor-mistral.git
   cd tradutor-mistral
   ```

2. Instale as dependências:
   ```bash
   poetry install
   ```

3. Crie um arquivo `.env` na raiz do projeto com sua chave API:
   ```
   MISTRAL_API_KEY=sua_chave_aqui
   ```

### Execução

Execute o aplicativo com:

```bash
poetry run streamlit run app.py
```

O aplicativo estará disponível em `http://localhost:8501` no seu navegador.

## 📝 Como Usar

1. Digite ou cole o texto que deseja traduzir no campo à esquerda
2. Selecione o idioma de destino no menu dropdown
3. Para idiomas não listados, marque a opção "Usar outro idioma" e digite o nome do idioma desejado
4. Clique no botão "Traduzir"
5. A tradução aparecerá no campo à direita

## 🔑 Obtendo uma Chave API

Para usar este aplicativo, você precisará de uma chave API da Mistral AI:

1. Acesse [mistral.ai](https://mistral.ai)
2. Registre-se para uma conta
3. Navegue até a seção de API ou chaves
4. Gere uma nova chave API
5. Adicione a chave ao arquivo `.env` ou insira-a diretamente no aplicativo

## 📜 Licença

Este projeto está licenciado sob [inserir tipo de licença aqui] - veja o arquivo LICENSE para detalhes.

## 👤 Autor

- [Seu Nome](https://github.com/paribe)

---

Desenvolvido com ❤️ usando Mistral AI e Streamlit