import justpy as jp

class About:

    path = "/about"
    def serve(self):
        wp = jp.QuasarPage()
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=wp, text="This is the about page!", classes = "text-4xl m-2")
        jp.Div(a=wp, text = "text", classes = "text-lg")

        return wp

