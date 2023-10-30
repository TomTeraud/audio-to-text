from tkinter import *
from tkinter import ttk
from typing import Protocol


class Presenter(Protocol):

    def handle_new_word_loading(self, event=None) -> None:
        ...

    def handle_new_sentence_loading(self, event=None) -> None:
        ...

    def handle_recording_start(self, event=None) -> None:
        ...

class PronouncePal(Protocol):
    frame = ttk.Frame



class MainPageWidgets():
    def __init__(self, parent:PronouncePal, presenter:Presenter) -> None:
        self.frame = parent.frame
        self.create_main_page_widgets()
        self.place_widgets_on_grid()
        self.setup_widgets_items(presenter)


    def create_main_page_widgets(self):
        self.new_word_button = ttk.Button(self.frame, text="Load new word")
        self.new_sentence_button = ttk.Button(self.frame, text="Load new sentence")
        self.rec_start_button = ttk.Button(self.frame, text="Start recording")
        self.sample_text_field = Text(self.frame, height=10, width=30, wrap="word")
        self.transcribed_text_field = Text(self.frame, height=10, width=30, wrap="word")

    def place_widgets_on_grid(self):
        self.new_word_button.grid(row=1, column=0, sticky=NSEW)
        self.new_sentence_button.grid(row=1, column=1, sticky=NSEW)
        self.rec_start_button.grid(row=1, column=2, sticky=NSEW, columnspan=2)
        self.sample_text_field.grid(row=0, column=0, sticky=NSEW, columnspan=2)
        self.transcribed_text_field.grid(row=0, column=2, sticky=NSEW, columnspan=2)

    def setup_widgets_items(self, presenter:Presenter):
        self.new_word_button.bind("<Button-1>", presenter.handle_new_word_loading)
        self.new_sentence_button.bind("<Button-1>", presenter.handle_new_sentence_loading)
        self.rec_start_button.bind("<Button-1>", presenter.handle_recording_start)


    def update_text_field(self, sample: str) -> None:
        self.sample_text_field.delete("1.0", END)
        self.sample_text_field.insert("1.0", sample)