import tkinter as tk
from tkinter import ttk
from gui.text_fields import SampleTextField, TranscribedTextField
from gui.button_manager import ButtonManager, LoadSampleButton, RecordButton, LoadWordSampleButton
from gui.menu.menu_bar import MenuBar
from gui.recording_progres_bar import RecordingProgresBar

class AudioRecorderGUI(tk.Tk):
    def __init__(self, text_sample):
        super().__init__()
        self.text_sample = text_sample

        self.title("Audio Recorder")
        self.geometry("600x300")
        self.setup_gui()

    def setup_gui(self):
        parent = ttk.Frame(self, borderwidth=20, relief="solid")
        parent.grid(sticky=(tk.N, tk.W, tk.E, tk.S))

        # Create the RecordingProgresBar widget, duration comes from text_sample
        self.progress_bar = RecordingProgresBar(parent, self.text_sample)
        self.progress_bar.grid(row=2, column=0, sticky="nsew", columnspan=4)

        self.sample_text_field = SampleTextField(parent, self.text_sample)
        self.sample_text_field.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.transcribed_text_field = TranscribedTextField(parent)
        self.transcribed_text_field.grid(row=0, column=2, sticky="nsew", columnspan=2)

        self.button_manager = ButtonManager()

        self.load_word_sample_button = LoadWordSampleButton(
            parent,
            self.text_sample,
            self.sample_text_field,
            button_manager=self.button_manager
        )
        self.load_word_sample_button.grid(row=1, column=0, sticky="nsew")

        self.load_sample_button = LoadSampleButton(
            parent,
            self.text_sample,
            self.sample_text_field,
            button_manager=self.button_manager
        )
        self.load_sample_button.grid(row=1, column=1, sticky="nsew")

        self.record_button = RecordButton(
            parent,
            self.text_sample,
            self.transcribed_text_field,
            self.button_manager,
            self.progress_bar,
        )
        self.record_button.grid(row=1, column=2, sticky="nsew", columnspan=2)

        self.menu_bar = MenuBar(self, self.text_sample, self.sample_text_field, self.button_manager)
        self.config(menu=self.menu_bar)

        # Apply columnconfigure to each column
        for col in range(4):
            parent.columnconfigure(col, weight=1)

        # Apply rowconfigure to each row
        for row in range(3):
            parent.rowconfigure(row, weight=1, minsize=30)

        for child in parent.winfo_children():
            child.grid_configure(padx=2, pady=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)