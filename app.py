import streamlit as st
#from PIL import Image
import os
import random

path = os.path.dirname(__file__)
#fichero = path+'/media/meme.jpg'
#imagen = Image.open(fichero)
#st.image(imagen, caption="Disaster girl meme",width=400)
#st.audio(path+"/media/call-the-police-18554.mp3")
#st.write('Music by [Gvidon](https://pixabay.com/users/gvidon-25326719/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=18554) from Pixabay')

lista_rock=[
    "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
    "https://youtu.be/bePCRKGUwAY"
]

lista_clasica=[
    "https://www.youtube.com/watch?v=7DBIR30ks64",
    "https://youtu.be/gkDbAWKkeX4"
]

st.header("Recomendamos música según tus gustos")
genero=st.radio("Rock","Clásica","Reggeton")
if genero=="Reggeton":
    st.write("Tienes que elegir música")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
if genero=="Rock":
    st.video(random.choice(lista_rock))
if genero=="Clásica":
    st.video(random.choice(lista_clasica))
