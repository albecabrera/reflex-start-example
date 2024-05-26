import reflex as rx
import link_bio.constants as const
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
            "https://www.twitch.tv/juliomv93",
            "twitch"
        ),
        link_button(
            "Youtube",
            "Canal de YouTube",
            "https://www.youtube.com/channel/UCaRhTIsmEQYwkrkb_iHmt9A",
            "youtube"
        ),
        link_button(
            "github",
            "Repositorio de GitHub",
            "https://github.com/JulioV93",
            "github"
        ),
        link_button(
            "Linkedin",
            "Perfil de Linkedin",
            "https://www.linkedin.com/in/julio-alejandro-machado/",
            "linkedin"
        ),
        title(
            "Personales"
        ),
        link_button(
            "Twitch",
            "Canal de Twitch",
            "https://www.twitch.tv/juliomv93",
            "twitch"
        ),
        link_button(
            "Youtube",
            "Canal de YouTube",
            "https://www.youtube.com/channel/UCaRhTIsmEQYwkrkb_iHmt9A",
            "youtube"
        ),
        link_button(
            "github",
            "Repositorio de GitHub",
            "https://github.com/JulioV93",
            "github"
        ),
        link_button(
            "Linkedin",
            "Perfil de Linkedin",
            "https://www.linkedin.com/in/julio-alejandro-machado/",
            "linkedin"
        ),
        title(
            "Contacto"
        ),
        link_button(
            "Email",
            const.EMAIL,
            f"mailti:{const.EMAIL}",
            "mail"
        ),
        width="100%"
    )