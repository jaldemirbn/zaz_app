# =====================================================
# zAz — MÓDULO 07
# ETAPA 07 — Canvas (Visual)
# =====================================================

# =====================================================
# IMPORTS
# =====================================================
import streamlit as st
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import io


# =====================================================
# HELPERS (LÓGICA PURA)
# =====================================================
def _abrir_imagem_segura(imagem_bytes):
    """
    Abre imagem de forma segura.
    Retorna Image ou None.
    """
    if not imagem_bytes or not isinstance(imagem_bytes, (bytes, bytearray)):
        return None

    try:
        return Image.open(io.BytesIO(imagem
