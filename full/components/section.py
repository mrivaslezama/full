import reflex as rx

def section() -> rx.Component:
    return rx.box(
    rx.section(
        rx.heading("First"),
        rx.text("This is the first content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    rx.section(
        rx.heading("Second"),
        rx.text("This is the second content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
        padding_bottom="20rem",
        margin_bottom="4rem"
    ),
    width="100%",
)