import tkinter as tk
from gui.menu._file_handler import FileMenuHandler
from gui.menu._help_handler import HelpMenuHandler
from gui.menu._rating_handler import RatingMenuHandler


class MenuBar(tk.Menu):
    def __init__(self, parent, text_sample, text_field_instance, button_manager):
        super().__init__(parent)
        self.text_sample = text_sample
        self.text_field_instance = text_field_instance
        self.button_manager = button_manager

        self.create_menus()

    def create_menus(self):
        self.create_file_menu()
        self.create_rating_menu()
        self.create_help_menu()

    def create_file_menu(self):
        menu_file = tk.Menu(self)
        self.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label="Add text file to database", command=self.handle_text_file_upload)
        menu_file.add_command(label="Delete all text samples from database", command=self.handle_text_samples_delete)
        # Add other file menu items as needed

    def handle_text_file_upload(self):
        result = FileMenuHandler.select_file()
        if result:
            self.update_gui()

    def handle_text_samples_delete(self):
        result = FileMenuHandler.delete_samples_from_db()
        if result:
            self.update_gui()

    def create_help_menu(self):
        menu_help = tk.Menu(self)
        self.add_cascade(menu=menu_help, label='Help')
        menu_help.add_command(label="Readme", command=HelpMenuHandler.show_readme)

    def create_rating_menu(self):
        menu_rating = tk.Menu(self)
        self.add_cascade(menu=menu_rating, label='Ratings')
        menu_rating.add_command(label="Sentences ratings", command=RatingMenuHandler.show_sentences_ratings)
        menu_rating.add_command(label="Words ratings", command=RatingMenuHandler.show_words_ratings)

    def update_gui(self):
        self.text_sample.update_sample()
        self.text_field_instance.update_text_sample()
        self.button_manager.update_buttons()
