import streamlit as st
from utils import search_arxiv, summarize_text
import pandas as pd

st.title("🧠 AI Literature Buddy")
query = st.text_input("Araştırma konunu gir:", placeholder="Örn: LLM agents for scientific reasoning")

if st.button("Ara ve Özetle"):
    if query:
        st.info("Makaleler aranıyor ve özetleniyor...")
        results = search_arxiv(query)
        data = []

        for title, summary, url in results:
            short_summary = summarize_text(summary)
            data.append({"Başlık": title, "Özet": short_summary, "Link": url})

        st.success("✅ Makaleler başarıyla özetlendi!")

        # 👇 Her bir makaleyi ayrı kutuda göster
        for i, row in enumerate(data):
            with st.expander(f"{i+1}. {row['Başlık']}"):
                st.markdown(f"**🔗 Link:** [{row['Link']}]({row['Link']})")
                st.markdown(f"**📝 Özet:** {row['Özet']}")
    else:
        st.warning("Lütfen bir konu gir.")


#Large Language Models for Question Answering

#Fikir → Literatür → Deney → Kod → Rapor
#      (PhD)       (Postdoc)  (MLE)   (Prof)
