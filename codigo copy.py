import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Configuração da página
st.set_page_config(
    page_title="Tradutor com Mistral AI",
    page_icon="🌐",
    layout="centered"
)

# Função para traduzir o texto
def traduzir_texto(texto, idioma, chave_api):
    # Inicializa o cliente Mistral com a chave API
    client = MistralClient(api_key=chave_api)

    # Define o modelo a ser usado
    modelo = "mistral-large-latest"

    # Função para invocar o modelo
    def invoke_model(model, messages):
        # Convert LangChain messages to Mistral format
        mistral_messages = []
        for msg in messages:
            if isinstance(msg, SystemMessage):
                role = "system"
            elif isinstance(msg, HumanMessage):
                role = "user"
            else:
                role = "assistant"

            mistral_messages.append(ChatMessage(role=role, content=msg.content))

        # Call the correct method
        response = client.chat(
            model=model,
            messages=mistral_messages
        )

        # Return the message content
        return response.choices[0].message.content

    parser = StrOutputParser()

    # Cria a cadeia de processamento
    chain = lambda messages: parser.invoke(invoke_model(modelo, messages))

    # Template de mensagem para tradução
    template_mensagem = ChatPromptTemplate.from_messages([
        ("system", "Traduza o texto a seguir para {idioma}"),
        ("user", "{texto}"),
    ])

    # Executa a tradução usando o template
    try:
        texto_traduzido = chain(template_mensagem.format_messages(
            idioma=idioma,
            texto=texto
        ))
        return texto_traduzido, None
    except Exception as e:
        return None, str(e)

# Função principal
def main():
    # Carrega variáveis de ambiente
    load_dotenv()

    # Título do app
    st.markdown("<h1 style='font-size: 24px;'>🌐 Tradutor com Mistral AI</h1>", unsafe_allow_html=True)
    st.write("Traduza textos para diversos idiomas usando inteligência artificial")

    # Sidebar para configuração
    with st.sidebar:
        #st.header("Configurações")

        # Chave API - usar secrets do Streamlit em produção!
        chave_api = os.getenv("MISTRAL_API_KEY")
        if not chave_api:
            chave_api = st.text_input("Mistral API Key", type="password")
            if not chave_api:
                st.error("Por favor, forneça uma chave API do Mistral")

    # Lista de idiomas
    idiomas = {
        "Inglês": "inglês",
        "Espanhol": "espanhol",
        "Francês": "francês",
        "Alemão": "alemão",
        "Italiano": "italiano",
        "Português": "português",
        "Japonês": "japonês",
        "Chinês": "chinês",
        "Russo": "russo",
        "Árabe": "árabe"
    }

    # Interface principal
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='font-size: 18px;'>Texto Original</h3>", unsafe_allow_html=True)
        texto_original = st.text_area("Digite o texto para traduzir em português", height=200)
        opcao_idioma = st.selectbox("Selecione o idioma de destino", list(idiomas.keys()))

        # Opção para idioma personalizado
        usar_outro_idioma = st.checkbox("Usar outro idioma")

        if usar_outro_idioma:
            idioma_personalizado = st.text_input("Digite o idioma desejado")
            idioma_destino = idioma_personalizado
        else:
            idioma_destino = idiomas[opcao_idioma]

        # Botão de tradução
        botao_traduzir = st.button("Traduzir", type="primary")

    with col2:
        st.markdown("<h3 style='font-size: 18px;'>Tradução</h3>", unsafe_allow_html=True)

        # Área para mostrar a tradução
        area_traducao = st.empty()

        # Container para mostrar o spinner durante a tradução
        with st.container():
            # Processar a tradução quando o botão for clicado
            if botao_traduzir and texto_original and chave_api:
                with st.spinner(f"Traduzindo para {idioma_destino}..."):
                    texto_traduzido, erro = traduzir_texto(texto_original, idioma_destino, chave_api)

                    if texto_traduzido:
                        area_traducao.text_area("Texto traduzido", value=texto_traduzido, height=200, disabled=True)
                        st.success("Tradução concluída!")
                    else:
                        area_traducao.empty()
                        st.error(f"Erro ao traduzir: {erro}")
            else:
                area_traducao.text_area("Texto traduzido", value="", height=200, disabled=True)

    # Informações adicionais
    with st.expander("Sobre o Tradutor"):
        st.write("""
        Este tradutor utiliza a API da Mistral AI em conjunto com o LangChain para fornecer
        traduções de alta qualidade. O modelo utilizado é o "mistral-large-latest", que oferece
        traduções precisas para diversos idiomas.

        Para usar este app, é necessário ter uma chave de API válida da Mistral AI.
        """)

if __name__ == "__main__":
    main()
