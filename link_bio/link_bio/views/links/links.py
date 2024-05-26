import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title(
            "Personales"
        ),
        link_button(
            "Twitch",
            "Canal de Twitch",
            "https://www.twitch.tv/juliomv93"
        ),
        link_button(
            "Youtube",
            "Canal de YouTube",
            "https://www.youtube.com/channel/UCaRhTIsmEQYwkrkb_iHmt9A"
        ),
        link_button(
            "github",
            "Repositorio de GitHub",
            "https://github.com/JulioV93"
        ),
        link_button(
            "Linkedin",
            "Perfil de Linkedin",
            "https://www.linkedin.com/in/julio-alejandro-machado/"
        ),
        title(
            "Personales"
        ),
        link_button(
            "Twitch",
            "Canal de Twitch",
            "https://www.twitch.tv/juliomv93"
        ),
        link_button(
            "Youtube",
            "Canal de YouTube",
            "https://www.youtube.com/channel/UCaRhTIsmEQYwkrkb_iHmt9A"
        ),
        link_button(
            "github",
            "Repositorio de GitHub",
            "https://github.com/JulioV93"
        ),
        link_button(
            "Linkedin",
            "Perfil de Linkedin",
            "https://www.linkedin.com/in/julio-alejandro-machado/"
        ),
        width="100%"
    )