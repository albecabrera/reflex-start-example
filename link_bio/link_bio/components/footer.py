import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="Logotipo de Reflex."
        ),
        rx.link(
            f"2023 - {datetime.date.today().year} ACWebdesign3",
            href="https://www.linkedin.com/in/julio-alejandro-machado/",
            is_external=True
        ),
        rx.text(
            "Software Engineer | Ingenierio en Computación e Informática",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value
    )