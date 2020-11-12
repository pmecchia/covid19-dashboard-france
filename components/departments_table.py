from utils.data import DF_DEP_TABLE
import dash_table
from dash_table.Format import Format
import pandas as pd




def departments_results(department):
    
    font_size = ".9vw"
    color_active = "#F4F4F4"
    color_inactive = "#AEAEAE"
    color_bg = "#000000"
    
    font_size_body = ".9vw"
    table = dash_table.DataTable(
        data=DF_DEP_TABLE.to_dict("records"),
        columns=[
            {"name": "Departments", "id": "Departments",},
            {
                "name": "Confirmed",
                "id": "Confirmed",
                "format": Format(group=","),
            },
            {
                "name": "Deaths",
                "id": "Deaths",
            },
        ],
        editable=False,
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        style_as_list_view=True,
        fixed_rows={"headers": True},
        fill_width=False,
        style_table={
            "width": "100%",
            "height": "100%",
        },
        style_header={
            "backgroundColor": color_bg,
            "border": color_bg,
            "fontWeight": "bold",
            "font": "Lato, sans-serif",
            "height": "2vw",
            "textAlign":'left',
            "padding": "1vw",
        },
        style_cell={
            "font-size": font_size_body,
            "font-family": "Lato, sans-serif",
            "border-left": "0",
            "border-right": "0",
            "border-bottom": "0.01rem solid #313841",
            "backgroundColor": "#000000",
            "border": "#000000",
            "color": "#FEFEFE",
            "height": "2.75vw",
            "width":"7vw",
            "textAlign":'center',
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "Departments",},
                #"minWidth": "4vw",
                #"width": "33%",
                #"maxWidth": "33%",
            },
            {
                "if": {"column_id": "Confirmed",},
                "color": "#dc9e00",
                #"minWidth": "4vw",
                #"width": "33%",
                #"maxWidth": "33%",
            },
            {
                "if": {"column_id": "Deaths",},
                "color": "#c94904",
                #"minWidth": "4vw",
                #"width": "33%",
                #"maxWidth": "33%",
            },
        ],
        #style_data_conditional=[                
            #{
            #    "if": {"state": "selected"},
            #    "backgroundColor": "inherit !important",
            #    "border": "inherit !important",
           # }  
        #],
    )

    return table