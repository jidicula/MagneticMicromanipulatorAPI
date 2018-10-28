#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 27, 2018 05:38:37 PM EDT  platform: Linux

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

import pagegui1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    pagegui1_support.set_Tk_var()
    top = GUI (root)
    pagegui1_support.init(root, top)
    root.mainloop()

w = None
def create_GUI(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    pagegui1_support.set_Tk_var()
    top = GUI (w)
    pagegui1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_GUI():
    global w
    w.destroy()
    w = None


class GUI:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family Verdana -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("756x587+141+75")
        top.title("GUI")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.MM_Frame = Frame(top)
        self.MM_Frame.place(relx=0.0, rely=0.0, relheight=0.503, relwidth=0.536)
        self.MM_Frame.configure(relief=RAISED)
        self.MM_Frame.configure(borderwidth="2")
        self.MM_Frame.configure(relief=RAISED)
        self.MM_Frame.configure(width=405)

        self.Entry_gtp_x = Entry(self.MM_Frame)
        self.Entry_gtp_x.place(relx=0.049, rely=0.136, height=20, relwidth=0.114)

        self.Entry_gtp_x.configure(background="white")
        self.Entry_gtp_x.configure(font="TkFixedFont")
        self.Entry_gtp_x.configure(selectbackground="#c4c4c4")

        self.Label_Manipulator = Label(self.MM_Frame)
        self.Label_Manipulator.place(relx=0.049, rely=0.034, height=28
                , width=136)
        self.Label_Manipulator.configure(activebackground="#f9f9f9")
        self.Label_Manipulator.configure(font=font9)
        self.Label_Manipulator.configure(text='''Micromanipulator''')

        self.Entry_gtp_y = Entry(self.MM_Frame)
        self.Entry_gtp_y.place(relx=0.173, rely=0.136, height=20, relwidth=0.114)

        self.Entry_gtp_y.configure(background="white")
        self.Entry_gtp_y.configure(font="TkFixedFont")
        self.Entry_gtp_y.configure(selectbackground="#c4c4c4")

        self.Entry_gtp_z = Entry(self.MM_Frame)
        self.Entry_gtp_z.place(relx=0.296, rely=0.136, height=20, relwidth=0.114)

        self.Entry_gtp_z.configure(background="white")
        self.Entry_gtp_z.configure(font="TkFixedFont")
        self.Entry_gtp_z.configure(selectbackground="#c4c4c4")

        self.Button_gtp = Button(self.MM_Frame)
        self.Button_gtp.place(relx=0.049, rely=0.203, height=26, width=149)
        self.Button_gtp.configure(activebackground="#d9d9d9")
        self.Button_gtp.configure(text='''Go To Position (um)''')

        self.Button_step_x = Button(self.MM_Frame)
        self.Button_step_x.place(relx=0.198, rely=0.508, height=26, width=32)
        self.Button_step_x.configure(activebackground="#d9d9d9")
        self.Button_step_x.configure(text='''x''')

        self.Label_step = Label(self.MM_Frame)
        self.Label_step.place(relx=0.049, rely=0.441, height=18, width=92)
        self.Label_step.configure(activebackground="#f9f9f9")
        self.Label_step.configure(text='''Move Step/um''')

        self.Button_step_y = Button(self.MM_Frame)
        self.Button_step_y.place(relx=0.198, rely=0.61, height=26, width=32)
        self.Button_step_y.configure(activebackground="#d9d9d9")
        self.Button_step_y.configure(text='''y''')

        self.Button_step_z = Button(self.MM_Frame)
        self.Button_step_z.place(relx=0.198, rely=0.712, height=26, width=32)
        self.Button_step_z.configure(activebackground="#d9d9d9")
        self.Button_step_z.configure(text='''z''')

        self.Button_setorigin = Button(self.MM_Frame)
        self.Button_setorigin.place(relx=0.049, rely=0.305, height=26, width=87)
        self.Button_setorigin.configure(activebackground="#d9d9d9")
        self.Button_setorigin.configure(text='''Set Origin''')

        self.Radiobutton_relative = Radiobutton(self.MM_Frame)
        self.Radiobutton_relative.place(relx=0.469, rely=0.102, relheight=0.068
                , relwidth=0.19)
        self.Radiobutton_relative.configure(activebackground="#d9d9d9")
        self.Radiobutton_relative.configure(justify=LEFT)
        self.Radiobutton_relative.configure(text='''Relative''')
        self.Radiobutton_relative.configure(value="relative")
        self.Radiobutton_relative.configure(variable=pagegui1_support.position_mode)

        self.Radiobutton_absolute = Radiobutton(self.MM_Frame)
        self.Radiobutton_absolute.place(relx=0.469, rely=0.169, relheight=0.068
                , relwidth=0.205)
        self.Radiobutton_absolute.configure(activebackground="#d9d9d9")
        self.Radiobutton_absolute.configure(justify=LEFT)
        self.Radiobutton_absolute.configure(text='''Absolute''')
        self.Radiobutton_absolute.configure(value="absolute")
        self.Radiobutton_absolute.configure(variable=pagegui1_support.position_mode)

        self.Button_velocity = Button(self.MM_Frame)
        self.Button_velocity.place(relx=0.494, rely=0.339, height=26, width=126)
        self.Button_velocity.configure(activebackground="#d9d9d9")
        self.Button_velocity.configure(text='''Change Velocity''')

        self.Entry_velocity = Entry(self.MM_Frame)
        self.Entry_velocity.place(relx=0.815, rely=0.339, height=20
                , relwidth=0.138)
        self.Entry_velocity.configure(background="white")
        self.Entry_velocity.configure(font="TkFixedFont")
        self.Entry_velocity.configure(selectbackground="#c4c4c4")

        self.Spinbox_step_x = Spinbox(self.MM_Frame, from_=-50.0, to=50.0)
        self.Spinbox_step_x.place(relx=0.099, rely=0.508, relheight=0.068
                , relwidth=0.094)
        self.Spinbox_step_x.configure(activebackground="#f9f9f9")
        self.Spinbox_step_x.configure(background="white")
        self.Spinbox_step_x.configure(from_="-50.0")
        self.Spinbox_step_x.configure(highlightbackground="black")
        self.Spinbox_step_x.configure(selectbackground="#c4c4c4")
        self.Spinbox_step_x.configure(textvariable=pagegui1_support.step_x)
        self.Spinbox_step_x.configure(to="50.0")

        self.Spinbox_step_z = Spinbox(self.MM_Frame, from_=-50.0, to=50.0)
        self.Spinbox_step_z.place(relx=0.099, rely=0.712, relheight=0.068
                , relwidth=0.094)
        self.Spinbox_step_z.configure(activebackground="#f9f9f9")
        self.Spinbox_step_z.configure(background="white")
        self.Spinbox_step_z.configure(from_="-50.0")
        self.Spinbox_step_z.configure(highlightbackground="black")
        self.Spinbox_step_z.configure(selectbackground="#c4c4c4")
        self.Spinbox_step_z.configure(textvariable=pagegui1_support.step_z)
        self.Spinbox_step_z.configure(to="50.0")

        self.Spinbox_step_y = Spinbox(self.MM_Frame, from_=-50.0, to=50.0)
        self.Spinbox_step_y.place(relx=0.099, rely=0.61, relheight=0.068
                , relwidth=0.094)
        self.Spinbox_step_y.configure(activebackground="#f9f9f9")
        self.Spinbox_step_y.configure(background="white")
        self.Spinbox_step_y.configure(from_="-50.0")
        self.Spinbox_step_y.configure(highlightbackground="black")
        self.Spinbox_step_y.configure(selectbackground="#c4c4c4")
        self.Spinbox_step_y.configure(textvariable=pagegui1_support.step_y)
        self.Spinbox_step_y.configure(to="50.0")

        self.Radiobutton_highres = Radiobutton(self.MM_Frame)
        self.Radiobutton_highres.place(relx=0.494, rely=0.508, relheight=0.068
                , relwidth=0.311)
        self.Radiobutton_highres.configure(activebackground="#d9d9d9")
        self.Radiobutton_highres.configure(justify=LEFT)
        self.Radiobutton_highres.configure(text='''High Resolution''')
        self.Radiobutton_highres.configure(value="high")
        self.Radiobutton_highres.configure(variable=pagegui1_support.radio_resolution)

        self.Radiobutton_lowres = Radiobutton(self.MM_Frame)
        self.Radiobutton_lowres.place(relx=0.494, rely=0.441, relheight=0.068
                , relwidth=0.299)
        self.Radiobutton_lowres.configure(activebackground="#d9d9d9")
        self.Radiobutton_lowres.configure(justify=LEFT)
        self.Radiobutton_lowres.configure(text='''Low Resolution''')
        self.Radiobutton_lowres.configure(value="low")
        self.Radiobutton_lowres.configure(variable=pagegui1_support.radio_resolution)

        self.Button_mm_interrupt = Button(self.MM_Frame)
        self.Button_mm_interrupt.place(relx=0.765, rely=0.881, height=26
                , width=81)
        self.Button_mm_interrupt.configure(activebackground="#d9d9d9")
        self.Button_mm_interrupt.configure(text='''Interrupt''')

        self.Current_Frame = Frame(top)
        self.Current_Frame.place(relx=0.0, rely=0.511, relheight=0.486
                , relwidth=0.536)
        self.Current_Frame.configure(relief=RAISED)
        self.Current_Frame.configure(borderwidth="2")
        self.Current_Frame.configure(relief=RAISED)
        self.Current_Frame.configure(width=405)

        self.Label_supply = Label(self.Current_Frame)
        self.Label_supply.place(relx=0.025, rely=0.035, height=23, width=175)
        self.Label_supply.configure(activebackground="#f9f9f9")
        self.Label_supply.configure(font=font9)
        self.Label_supply.configure(text='''Current/Power Supply''')

        self.Entry_amps = Entry(self.Current_Frame)
        self.Entry_amps.place(relx=0.296, rely=0.105,height=20, relwidth=0.114)
        self.Entry_amps.configure(background="white")
        self.Entry_amps.configure(font="TkFixedFont")
        self.Entry_amps.configure(selectbackground="#c4c4c4")

        self.Label_amps = Label(self.Current_Frame)
        self.Label_amps.place(relx=0.025, rely=0.105, height=18, width=87)
        self.Label_amps.configure(activebackground="#f9f9f9")
        self.Label_amps.configure(text='''Amperes (mA)''')

        self.Label_duration = Label(self.Current_Frame)
        self.Label_duration.place(relx=0.025, rely=0.175, height=18, width=79)
        self.Label_duration.configure(activebackground="#f9f9f9")
        self.Label_duration.configure(text='''Duration (s)''')

        self.Entry_duration = Entry(self.Current_Frame)
        self.Entry_duration.place(relx=0.296, rely=0.175, height=20
                , relwidth=0.114)
        self.Entry_duration.configure(background="white")
        self.Entry_duration.configure(font="TkFixedFont")
        self.Entry_duration.configure(selectbackground="#c4c4c4")

        self.Entry_frequency = Entry(self.Current_Frame)
        self.Entry_frequency.place(relx=0.296, rely=0.246, height=20
                , relwidth=0.114)
        self.Entry_frequency.configure(background="white")
        self.Entry_frequency.configure(font="TkFixedFont")
        self.Entry_frequency.configure(selectbackground="#c4c4c4")

        self.Label_frequency = Label(self.Current_Frame)
        self.Label_frequency.place(relx=0.025, rely=0.246, height=18, width=104)
        self.Label_frequency.configure(activebackground="#f9f9f9")
        self.Label_frequency.configure(text='''Frequency (kHz)''')

        self.Label_shape = Label(self.Current_Frame)
        self.Label_shape.place(relx=0.025, rely=0.316, height=18, width=44)
        self.Label_shape.configure(activebackground="#f9f9f9")
        self.Label_shape.configure(text='''Shape''')

        self.Button_configuration = Button(self.Current_Frame)
        self.Button_configuration.place(relx=0.074, rely=0.632, height=26
                , width=135)
        self.Button_configuration.configure(activebackground="#d9d9d9")
        self.Button_configuration.configure(text='''Set Configuration''')

        self.Button_begin = Button(self.Current_Frame)
        self.Button_begin.place(relx=0.469, rely=0.105, height=26, width=125)
        self.Button_begin.configure(activebackground="#d9d9d9")
        self.Button_begin.configure(text='''Begin Experiment''')

        self.Button_stop = Button(self.Current_Frame)
        self.Button_stop.place(relx=0.469, rely=0.211, height=26, width=119)
        self.Button_stop.configure(activebackground="#d9d9d9")
        self.Button_stop.configure(text='''Stop Experiment''')

        self.Button_ps_interrupt = Button(self.Current_Frame)
        self.Button_ps_interrupt.place(relx=0.765, rely=0.877, height=26
                , width=81)
        self.Button_ps_interrupt.configure(activebackground="#d9d9d9")
        self.Button_ps_interrupt.configure(text='''Interrupt''')

        self.Button_current = Button(self.Current_Frame)
        self.Button_current.place(relx=0.074, rely=0.737, height=26, width=125)
        self.Button_current.configure(activebackground="#d9d9d9")
        self.Button_current.configure(text='''Change Current''')

        self.Radiobutton_shape1 = Radiobutton(self.Current_Frame)
        self.Radiobutton_shape1.place(relx=0.148, rely=0.316, relheight=0.07
                , relwidth=0.188)
        self.Radiobutton_shape1.configure(activebackground="#d9d9d9")
        self.Radiobutton_shape1.configure(justify=LEFT)
        self.Radiobutton_shape1.configure(text='''Shape1''')
        self.Radiobutton_shape1.configure(value="shape1")
        self.Radiobutton_shape1.configure(variable=pagegui1_support.shape)

        self.Radiobutton_shape2 = Radiobutton(self.Current_Frame)
        self.Radiobutton_shape2.place(relx=0.148, rely=0.386, relheight=0.07
                , relwidth=0.188)
        self.Radiobutton_shape2.configure(activebackground="#d9d9d9")
        self.Radiobutton_shape2.configure(justify=LEFT)
        self.Radiobutton_shape2.configure(text='''Shape2''')
        self.Radiobutton_shape2.configure(value="shape2")
        self.Radiobutton_shape2.configure(variable=pagegui1_support.shape)

        self.Radiobutton_shape3 = Radiobutton(self.Current_Frame)
        self.Radiobutton_shape3.place(relx=0.148, rely=0.456, relheight=0.07
                , relwidth=0.188)
        self.Radiobutton_shape3.configure(activebackground="#d9d9d9")
        self.Radiobutton_shape3.configure(justify=LEFT)
        self.Radiobutton_shape3.configure(text='''Shape3''')
        self.Radiobutton_shape3.configure(value="shape3")
        self.Radiobutton_shape3.configure(variable=pagegui1_support.shape)

        self.Radiobutton_shape4 = Radiobutton(self.Current_Frame)
        self.Radiobutton_shape4.place(relx=0.148, rely=0.526, relheight=0.07
                , relwidth=0.188)
        self.Radiobutton_shape4.configure(activebackground="#d9d9d9")
        self.Radiobutton_shape4.configure(justify=LEFT)
        self.Radiobutton_shape4.configure(text='''Shape4''')
        self.Radiobutton_shape4.configure(value="shape4")
        self.Radiobutton_shape4.configure(variable=pagegui1_support.shape)

        self.Status_Frame = Frame(top)
        self.Status_Frame.place(relx=0.542, rely=0.0, relheight=0.724
                , relwidth=0.456)
        self.Status_Frame.configure(relief=RAISED)
        self.Status_Frame.configure(borderwidth="2")
        self.Status_Frame.configure(relief=RAISED)
        self.Status_Frame.configure(width=345)

        self.Label_status = Label(self.Status_Frame)
        self.Label_status.place(relx=0.029, rely=0.024, height=23, width=54)
        self.Label_status.configure(activebackground="#f9f9f9")
        self.Label_status.configure(font=font9)
        self.Label_status.configure(text='''Status''')

        self.Label_status_position = Label(self.Status_Frame)
        self.Label_status_position.place(relx=0.058, rely=0.094, height=18
                , width=128)
        self.Label_status_position.configure(activebackground="#f9f9f9")
        self.Label_status_position.configure(text='''Position (um): x, y, z''')

        self.Label_status_posmode = Label(self.Status_Frame)
        self.Label_status_posmode.place(relx=0.058, rely=0.141, height=18
                , width=100)
        self.Label_status_posmode.configure(activebackground="#f9f9f9")
        self.Label_status_posmode.configure(text='''Position Mode:''')

        self.Label_status_resolution = Label(self.Status_Frame)
        self.Label_status_resolution.place(relx=0.058, rely=0.235, height=18
                , width=74)
        self.Label_status_resolution.configure(activebackground="#f9f9f9")
        self.Label_status_resolution.configure(text='''Resolution:''')

        self.Label_status_amps = Label(self.Status_Frame)
        self.Label_status_amps.place(relx=0.058, rely=0.306, height=18, width=96)

        self.Label_status_amps.configure(activebackground="#f9f9f9")
        self.Label_status_amps.configure(text='''Amperes (mA):''')

        self.Label_status_duration = Label(self.Status_Frame)
        self.Label_status_duration.place(relx=0.058, rely=0.353, height=18
                , width=127)
        self.Label_status_duration.configure(activebackground="#f9f9f9")
        self.Label_status_duration.configure(text='''Time Remaining (s):''')

        self.Label_status_frequency = Label(self.Status_Frame)
        self.Label_status_frequency.place(relx=0.058, rely=0.4, height=18
                , width=108)
        self.Label_status_frequency.configure(activebackground="#f9f9f9")
        self.Label_status_frequency.configure(text='''Frequency (kHz):''')

        self.Label_status_velocity = Label(self.Status_Frame)
        self.Label_status_velocity.place(relx=0.058, rely=0.188, height=18
                , width=107)
        self.Label_status_velocity.configure(activebackground="#f9f9f9")
        self.Label_status_velocity.configure(text='''Velocity (units?):''')

        self.Label_status_shape = Label(self.Status_Frame)
        self.Label_status_shape.place(relx=0.058, rely=0.447, height=18
                , width=48)
        self.Label_status_shape.configure(activebackground="#f9f9f9")
        self.Label_status_shape.configure(text='''Shape:''')

        self.Label_magnetic_field = Label(self.Status_Frame)
        self.Label_magnetic_field.place(relx=0.058, rely=0.518, height=18
                , width=120)
        self.Label_magnetic_field.configure(activebackground="#f9f9f9")
        self.Label_magnetic_field.configure(text='''Magnetic Field (B):''')

        self.Label_console = Label(self.Status_Frame)
        self.Label_console.place(relx=0.058, rely=0.588, height=18, width=101)
        self.Label_console.configure(activebackground="#f9f9f9")
        self.Label_console.configure(text='''Console Output''')

        self.Message_console = Message(self.Status_Frame)
        self.Message_console.place(relx=0.058, rely=0.635, relheight=0.353
                , relwidth=0.893)
        self.Message_console.configure(anchor=NW)
        self.Message_console.configure(background="#ffffff")
        self.Message_console.configure(highlightbackground="#d8d8d8")
        self.Message_console.configure(relief=SUNKEN)
        self.Message_console.configure(text='''Messages''')
        self.Message_console.configure(width=308)

        self.Frame_demag = Frame(top)
        self.Frame_demag.place(relx=0.542, rely=0.733, relheight=0.264
                , relwidth=0.456)
        self.Frame_demag.configure(relief=RAISED)
        self.Frame_demag.configure(borderwidth="2")
        self.Frame_demag.configure(relief=RAISED)
        self.Frame_demag.configure(width=345)

        self.Button_demag = Button(self.Frame_demag)
        self.Button_demag.place(relx=0.145, rely=0.323, height=58, width=240)
        self.Button_demag.configure(activebackground="#d9d9d9")
        self.Button_demag.configure(text='''Start Demagnetization Process''')
        self.Button_demag.configure(width=240)

        self.Label1 = Label(self.Frame_demag)
        self.Label1.place(relx=0.145, rely=0.774, height=18, width=193)
        self.Label1.configure(text='''tkinter messagebox for popup''')

    def getpos():

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



