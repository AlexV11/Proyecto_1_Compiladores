import streamlit as st
import ply.lex as lex
import re

tokens = ['LENG', 'OTRO']
t_LENG = r'a(b|c)*dcc(b|d)+aa'
t_OTRO = r'.'

st.write(
    '''
    338803 - Saul Fernando Rodríguez Gutiérrez
    338817 - Eric Alejandro Aguilar Marcial
    338931 - Andrés Alexis Villalba García
    '''
)

def revisar(cadena):
    aceptador = lex.lex()
    aceptador.input(cadena)
    el_token = aceptador.token()

    if re.match(t_LENG, el_token.value):
        st.success("La cadena pertenece a la lengua")
    else:
        st.error("La cadena no pertenece a la lengua")

st.title("Proyecto")
st.write("Sea un lenguaje como en L1 = a(b|c)∗d y sea un segundo lenguaje como en L2 = cc(b|d)+aa. Hagamos un aceptador de cadenas para el lenguaje L3 = L1L2. El aceptador de cadenas debe pedir la cadena al usuario y responder si le acepta o no lo hace.")

st.text_input("Ingrese una cadena:", key="cadena")
if st.button("Revisar"):
    revisar(st.session_state.cadena)
