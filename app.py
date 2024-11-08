import streamlit as st
from PIL import Image
import os

# Função para comparar o nome da imagem do usuário com o nome da imagem na pasta
def comparar_imagens(imagem_usuario, pasta_imagens):
    nome_usuario = os.path.splitext(imagem_usuario.name)[0].lower()  # Pega o nome da imagem sem a extensão e em minúsculas

    melhor_correspondencia = None
    descricao_completa = ""

    # Percorrer todas as imagens na pasta
    for arquivo in os.listdir(pasta_imagens):
        caminho_imagem = os.path.join(pasta_imagens, arquivo)

        if os.path.isfile(caminho_imagem) and caminho_imagem.endswith(('.jpg', '.jpeg', '.png')):
            # Pega o nome do arquivo sem a extensão e em minúsculas
            nome_arquivo_pasta = os.path.splitext(arquivo)[0].lower()

            # Verifica se o nome da imagem do usuário está no nome do arquivo da imagem na pasta
            if nome_usuario in nome_arquivo_pasta:
                descricao_completa = arquivo  # A descrição completa é o nome do arquivo
                melhor_correspondencia = caminho_imagem
                break  # Só precisamos da primeira correspondência, já que o nome é único

    return descricao_completa, melhor_correspondencia

# Função principal do Streamlit
def main():
    st.title("Reconhecimento e Comparação de Imagens")
    st.write("Envie uma imagem e ela será comparada com as imagens da pasta. A descrição será baseada na imagem mais similar.")

    # Subir arquivo de imagem
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Exibir imagem do usuário
        imagem_usuario = Image.open(uploaded_file)
        st.image(imagem_usuario, caption="Imagem enviada pelo usuário.", use_column_width=True)

        # Definir o caminho da pasta de imagens (agora com o nome "imagens")
        pasta_imagens = 'imagens'  # Aqui está o caminho da pasta de imagens

        # Verificar se a pasta existe
        if os.path.exists(pasta_imagens):
            st.write("Analisando a imagem...")

            # Comparar a imagem do usuário com as imagens na pasta
            descricao, imagem_correspondente = comparar_imagens(uploaded_file, pasta_imagens)

            if descricao:
                st.write(f"A descrição da imagem mais similar é: {descricao}")
                st.image(imagem_correspondente, caption="Imagem mais similar encontrada.", use_column_width=True)
            else:
                st.write("Nenhuma imagem similar encontrada na pasta.")
        else:
            st.write("Pasta de imagens não encontrada. Crie a pasta 'imagens' com as imagens e suas descrições.")

if __name__ == "__main__":
    main()
