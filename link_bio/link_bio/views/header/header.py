import reflex as rx

def header () -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Julio Machado", size="9"),     
        rx.text("@JulioV93") ,
        rx.text("Hola, mi nombre es Julio Machado"),
        rx.text("Ingeniero en Software e informática, con una sólida formación en el desarrollo de sistemas y aplicaciones. Cuento con más de 5 años de experiencia en la resolución de desafíos tecnológicos utilizando javascript, PHP, python, AzureDevOps, GIT, Bitbucket."),
        align="center"
    )