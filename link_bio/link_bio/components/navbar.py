import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Julio",
                as_="span",
                color=Color.PRIMARY.value
            ),
            rx.text(
                "MV93",
                as_="span",
                color=Color.SECONDARY.value
            )
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )