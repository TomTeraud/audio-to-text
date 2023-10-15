import tkinter as tk
from menu_bar._file_handler import FileMenuHandler as FMH
from menu_bar._help_handler import HelpMenuHandler as HMH
from menu_bar._rating_handler import RatingMenuHandler as RMH
from title_page.controler import ButtonState as BS


class MenuInitiator(tk.Menu):
    def __init__(self, parent, text_sample = None, text_field_instance = None, button_manager = None):
        super().__init__(parent)
        self.arg = parent
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.button_manager = button_manager

        self.create_menus()

    def create_menus(self):
        if BS.ready_to_start:
            self.create_file_menu()
        self.create_rating_menu()
        self.create_help_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        print(self.text_field_instance)
        print("+++++++++++++")
        menu_file.add_command(
        label="Add text file to database",
        command=lambda: FMH.handle_text_file_upload_with_args(
            self.text_sample,
            self.text_field_instance,
            self.button_manager
            ))
        menu_file.add_command(
            label="Delete all text samples from database", 
            command=lambda:FMH.handle_text_samples_delete_with_args(
            self.text_sample,
            self.text_field_instance,
            self.button_manager
            ))
        menu_file.add_command(
            label="Change transcriber", 
            command=lambda:FMH.handle_change_transcriber(
                self.arg
            ))

    def create_rating_menu(self):
        menu_rating = tk.Menu(self)
        self.add_cascade(menu=menu_rating, label='Ratings')
        menu_rating.add_command(label="Sentences ratings", command=RMH.show_sentences_ratings)
        menu_rating.add_command(label="Words ratings", command=RMH.show_words_ratings)

    def create_help_menu(self):
        menu_help = tk.Menu(self)
        self.add_cascade(menu=menu_help, label='Help')
        menu_help.add_command(label="Readme", command=HMH.show_readme)