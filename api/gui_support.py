#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 31, 2018 02:59:25 AM EDT  platform: Linux

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global gtp_x
    gtp_x = StringVar()
    global gtp_y
    gtp_y = StringVar()
    global gtp__z
    gtp__z = StringVar()
    global position_mode
    position_mode = StringVar()
    global velocity
    velocity = StringVar()
    global step_x
    step_x = StringVar()
    global step_z
    step_z = StringVar()
    global step_y
    step_y = StringVar()
    global radio_resolution
    radio_resolution = StringVar()
    global constant_amps
    constant_amps = StringVar()
    global constant_duration
    constant_duration = StringVar()
    global square_amps
    square_amps = StringVar()
    global square_duration
    square_duration = StringVar()
    global square_duty
    square_duty = StringVar()
    global square_freq
    square_freq = StringVar()
    global status_pos
    status_pos = StringVar()
    global status_posmode_v
    status_posmode_v = StringVar()
    global status_vel_v
    status_vel_v = StringVar()
    global status_res_v
    status_res_v = StringVar()
    global status_magfield_v
    status_magfield_v = StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()


