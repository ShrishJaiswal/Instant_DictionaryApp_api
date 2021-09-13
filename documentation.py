import justpy as jp
from justpy import tailwind
from pandas.core.dtypes.common import classes

class Doc:


    def serve(self):
        wp=jp.WebPage()


        div=jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is an api for Instant Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get Definition of words:", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=Farmer")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "Farmer", 
        "definition": ["One who farms", "One who hires and cultivates a farm; a cultivator of leased ground; a tenant.", "One who is devoted to the tillage of the soil; one who cultivates a farm; an agriculturist; a husbandman.", "One who takes taxes, customs, excise, or other duties, to collect, either paying a fixed annuual rent for the privilege; as, a farmer of the revenues.", "The lord of the field, or one who farms the lot and cope of the crown."]}""")

        return wp