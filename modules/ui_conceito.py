# 🎨 Abrir ImageFX (ALINHADO E MESMA ALTURA)
with col3:

    st.markdown("""
        <style>
        div[data-testid="stLinkButton"] a {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            height: 38px !important;
            padding: 0 16px !important;
            color: #FF9D28 !important;
            font-weight: 600;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    st.link_button(
        "🎨 Gerar imagens",
        "https://labs.google/fx/tools/image-fx",
        use_container_width=True
    )
