import streamlit as st

st.title("Sistema de Biblioteca")

#Criar lista de livros
if"livros" not in st.session_state:
    st.session_state.livros = []

#Cadastrar livro
    st.subheader("Cadastrar Livro")
    nome_livro = st.text_input("Nome do Livro")
    autor = st.text_input("Autor")

#Botão cadastrar 
    if st.button("Cadastrar Livro"):

        if nome_livro != "" and autor !="":
            livro ={
                    "nome": nome_livro,
                    "autor": autor,
                    "emprestado": False

            }
            st.session_state.livros.append(livro)
            st.success("lirvo cadastrado com sucesso")

#Listar livros
st.subheader("Livro Cadastrado")
if len(st.session_state.livros) == 0:
    st.warning("Nenhum livro cadastrado")
else:
    for i, livro in enumerate(st.session_state.livros):
            st.write(f"{livro["nome"]}")
            st.write(f"autor:{livro["autor"]}")

            if livro["emprestado"]== False :
                st.success("Disponivel")
            else:
                st.error("emprestado")
            col1, col2 = st.columns(2)

            #emprestimo
            with col1:
                if st.button("emprestar",key=f"emp{i}"):
                    st.session_state.livros[i]["emprestado"] = True
                    st.rerun()
        
#Devolução
            with col2:
                if st.button("devolvedor",key=f"dev{i}"):
                    st.session_state.livros[i]["emprestado"] = False
                    st.rerun
            st.divider()