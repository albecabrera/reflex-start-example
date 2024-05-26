import reflex as rx
import link_bio.styles.styles as styles


def link_icon(url: str, icon: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon
        ),
        href=url,
        is_external=True,
    )