import flet as ft


def main(page: ft.Page):
    page.add(
        ft.SafeArea(ft.Text("Hello, Flet!", size=30, weight="bold", color="red"))
    )


ft.app(main)
