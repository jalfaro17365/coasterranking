
import streamlit as st
import random
import os
import json

COASTERS_FILE = "coasters.txt"
RESULTS_FILE = "duel_results.json"

with open(COASTERS_FILE, "r", encoding="utf-8") as f:
    coasters = [line.strip() for line in f if line.strip()]

if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        results = json.load(f)
else:
    results = {}

all_duels = [(a, b) for i, a in enumerate(coasters) for b in coasters[i+1:]]
duels = [duel for duel in all_duels if f"{duel[0]} vs {duel[1]}" not in results]

st.title("Liga de Montañas Rusas 🎢")
st.write(f"Total de duelos restantes: {len(duels)}")

if duels:
    duel = duels[0]
    st.subheader("¿Cuál prefieres?")
    col1, col2 = st.columns(2)
    if col1.button(duel[0]):
        results[f"{duel[0]} vs {duel[1]}"] = duel[0]
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        st.experimental_rerun()
    if col2.button(duel[1]):
        results[f"{duel[0]} vs {duel[1]}"] = duel[1]
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        st.experimental_rerun()
else:
    st.success("¡Has completado todos los enfrentamientos!")
    scores = {name: 0 for name in coasters}
    for winner in results.values():
        scores[winner] += 1
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    st.subheader("Clasificación final (Top 20)")
    for i, (name, points) in enumerate(sorted_scores[:20], 1):
        st.write(f"{i}. {name} - {points} victorias")
