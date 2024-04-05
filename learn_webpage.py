import justpy as jp

"""This is with tailwind (css framework)"""
@jp.SetRoute("/home")
#"""Code is tied to this function"""
def home():
    wp = jp.Webpage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1= jp.Div(a=div, classes= "grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a =div1, placeholder="Enter first value",
                    classes="form-input")
    in_2 = jp.Input(a =div1, placeholder = "Enter second value",
                    classes="form-input")

    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-gray-400")
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div1, text="Calculate", click = sum_up, in1 = in_1, in2=in_2,
              d = d_output,
              classes ="border-blue-500 m-2 p-2 px-4 rounded"
              "text-blue-600 hover:bg-red-500 hover: text-white")
    jp.Div(a=div2, text="I am a cool interactive dive", mouseenter= mouse_enter,
           mouseleave = mouse_leave,
           classes = "hover_bg-red-500")
    jp.Input()



    return wp

@jp.SetRoute("/home")
#"""Code is tied to this function"""
def about():
    wp = jp.WebPage()
    jp.Div(a = wp, text="this page is very important")
    jp.Div(a = wp, text = "hello again")
    return wp

def sum_up(widget, msg):
    sum = float(widget.inpu1.value) + float(widget.input2.value)
    widget.d.text = sum

def mouse_enter(widget, msg):
    widget.text= "A mouse entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left!"

jp.justpy()



"""This is the same code, this time using Quasar. With 'Tailwind = True' we can still use Tailwind"""
@jp.SetRoute("/home")
#"""Code is tied to this function"""
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1= jp.Div(a=div, classes= "grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a =div1, placeholder="Enter first value",
                    classes="form-input")
    in_2 = jp.Input(a =div1, placeholder = "Enter second value",
                    classes="form-input")

    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-gray-400")
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.QBtn(a=div1,  color= "primary" , label = "secondary", text="Calculate", click = sum_up, in1 = in_1, in2=in_2,
              d = d_output,
              )
    jp.Div(a=div2, text="I am a cool interactive dive", mouseenter= mouse_enter,
           mouseleave = mouse_leave,
           classes = "hover_bg-red-500")
    jp.Input()



    return wp




@jp.SetRoute("/home")
#"""Code is tied to this function"""
def about():
    wp = jp.QuasarPage()
    jp.Div(a = wp, text="this page is very important")
    jp.Div(a = wp, text = "hello again")
    return wp

def sum_up(widget, msg):
    sum = float(widget.inpu1.value) + float(widget.input2.value)
    widget.d.text = sum

def mouse_enter(widget, msg):
    widget.text= "A mouse entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left!"
