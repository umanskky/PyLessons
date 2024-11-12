
""""
import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")


def prin():
    print("float")
    

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", )
    dpg.add_slider_float(label="float",default_value=25, min_value=25, callback=prin)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

"""

import dearpygui.dearpygui as dpg
from math import sin, cos

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))

def update_series():

    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * i / 1000))
    dpg.set_value('series_tag', [cosdatax, cosdatay])
    dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")

with dpg.window(label="Tutorial", tag="win"):
    dpg.add_button(label="Update Series", callback=update_series)
    # create plot
    with dpg.plot(label="Line Series", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis", tag="series_tag")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()