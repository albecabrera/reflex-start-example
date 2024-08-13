import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="JM",
                size="6",
                src="/avatarCabrera.png",
                radius="full",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border=f"4px solid {Color.PRIMARY.value}"
            ),
            rx.vstack(
                rx.heading(
                    "Alberto Cabrera",
                    size="4"
                ),
                rx.text(
                    "@albertocabrera",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/", "linkedin", "linkedin"),
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/", "github", "github"),
                    link_icon("https://www.linkedin.com/in/julio-alejandro-machado/", "youtube", "youtube"),
                ),
                align_items="start"
            ),
            spacing="4",
        ),
        rx.flex(
            info_text("+2", "años de experiencia"),
            rx.spacer(),
            
            info_text("+10", "aplicaciones creadas"),
            rx.spacer(),
        ),
        rx.text(
            "Soy Fullstack Developer y mi pasión es crear aplicaciones web. Cuento con más de 2 años de experiencia en la resolución de desafíos tecnológicos utilizando HTML, CSS, JS, PHP, Python, GIT y Frameworks como React y Astro.",
            color=TextColor.BODY.value
        ),
        spacing="4",
        align_items="start"
    )