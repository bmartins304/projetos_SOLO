import armazenar_prots
import transformar_ler_pdf2jpeg
import customtkinter as ctk
from tkinter import filedialog , messagebox
import os
from pdf2image import convert_from_path
from fpdf import FPDF
import shutil
import fitz

class ModernInterface():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("SARA Ver.0.0.1")
        self.root.geometry("1280x720")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20,fill="both",expand=True)

        # area de selecão do arquivo
        file_frame = ctk.CTkFrame(main_frame, fg_color="green")
        file_frame.pack(fill="x", pady=10)

        self.file_label = ctk.CTkLabel(
            file_frame,
            text="Nenhum arquivo selecionado",
            font=("Helvetica",14),
            wraplength=400
        )

        self.file_label.pack(side="left", fill="x", expand=True)
 

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernInterface()
    app.run()