import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2018 - {datetime.date.today().year} JulioMV93",
            href="https://www.linkedin.com/in/julio-alejandro-machado/",
            is_external=True
        ),
        rx.text("Software Engineer | Ingenierio en Computación e Informática")
    )