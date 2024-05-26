import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.twitch.tv/juliomv93"),
        link_button("Youtube", "https://www.youtube.com/channel/UCaRhTIsmEQYwkrkb_iHmt9A"),
        link_button("github", "https://github.com/JulioV93"),
        link_button("Linkedin", "https://www.linkedin.com/in/julio-alejandro-machado/")
    )