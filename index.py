import streamlit as st

#titulo
st.title("Sistema de Biblioteca")

#Criar lista de livros
if "livros" not in st.session_state:
    st.session_state.livros = []

#Cadastrar Livro
st.subheader("Cadastrar Livro")
nome_livro = st.text_input("Nome do Livro")
autor = st.text_input("Autor")

#Botão cadastrar
if st.button("Cadastrar Livro"):
    if nome_livro != "" and autor != "":
        livro = { 
            "nome": nome_livro,
            "autor": autor,
            "emprestado": False
        }
        st.session_state.livros.append(livro)
        st.success("Livro cadastrado com sucesso")

#Listar livros
st.subheader("Livro Cadastrados")
if len(st.session_state.livros) == 0:
    st.warning("Nenhum livro cadastrado")
   
else:
    for i, livro in enumerate(st.session_state.livros):
        st.write(f"{livro['nome']}")
        st.write(f"Autor:{livro['autor']}")
        if livro["emprestado"] == False:
            st.success("Disponível")
        else:
            st.error("Emprestado")
        col1, col2 = st.columns(2)
        
        #Empréstimo
        with col1:
            if st.button("Emprestar",key=f"emp{i}"):
                st.session_state.livros[i]["emprestado"] = True
                st.rerun()

        #Devolução
        with col2:
            if st.button("Devolvedor",key=f"dev{i}"):
                st.session_state.livros[i]["emprestado"] = False
                st.rerun()
        st.divider()