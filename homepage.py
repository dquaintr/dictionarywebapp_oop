import justpy as jp

class Home:
    path= "/home"

    def serve(self):
        wp = jp.Quasarpage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=wp, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=wp, text="text", classes="text-lg")

        return wp


