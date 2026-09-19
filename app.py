from data import graph, coord
from algorithm import greedy_bfs, a_star

import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>Tugas 2 KKA : Informed Search</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Farrel Satria Mukti - 5025251138 - KKA (A)</p>", 
    unsafe_allow_html=True
)
st.page_link("https://github.com/farrelsatria/kka-tugas2", label="*Klik disini untuk melihat dokumentasi repo.*", icon="🔗")

st.image("img/romania-map.png")

start = st.selectbox("Pilih Kota Asal", list(graph.keys()))
dest =  st.selectbox("Pilih Kota Tujuan", list(graph.keys()))
algorithm = st.selectbox("Pilih Algoritma", ["Greedy Best-First Search", "A* Search"])

if st.button("Cari Rute"):
    if algorithm == "Greedy Best-First Search":
        path, cost = greedy_bfs(graph, coord, start, dest)
    else:
        path, cost = a_star(graph, coord, start, dest)

    if path is None:
        st.error(f"Rute dari kota {start} menuju kota {dest} tidak ditemukan!")
    else:
        rute = " -> ".join(path)
        st.write("**Rute:**", rute)
        st.write("**Cost:**", cost)