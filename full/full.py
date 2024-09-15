"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar
from .components.footer import footer
from .components.section import section

class State(rx.State):
    """The app state."""
    label = "Bienvenidos a mi blog"

    def change_label(self):
        self.label = "Blog sobre mis opiniones y analisis."


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.label, "Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
           
            rx.link(
                rx.button("Check out our docs!", on_click=State.change_label),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        section(),
        footer(),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
