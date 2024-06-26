from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Watermark App")

        # Create a menu
        self.menu = Menu(master)
        master.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Upload Image", command=self.upload_image)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save Image", command=self.save_image, state=DISABLED)
        self.file_menu.add_command(label="Rotate Image", command=self.rotate_image, state=DISABLED)

        self.watermark_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Watermark", menu=self.watermark_menu)
        self.watermark_menu.add_command(label="Add Watermark", command=self.add_watermark, state=DISABLED)
        self.watermark_menu.add_command(label="Edit Watermark", command=self.edit_watermark, state=DISABLED)
        self.watermark_menu.add_command(label="Remove Watermark", command=self.remove_watermark, state=DISABLED)

        # Create canvas for displaying image
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.image = None
        self.original_image = None
        self.watermark_text = ""

    def upload_image(self):
        # Open file dialog to select image
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.original_image = self.image.copy()

            # Resize image if necessary
            if self.image.size[0] > 400 or self.image.size[1] > 400:
                self.image.thumbnail((400, 400))
                self.original_image = self.image.copy()

            # Display image on canvas
            self.photo_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

            # Enable buttons
            self.file_menu.entryconfig(3, state=NORMAL)  # Save Image
            self.file_menu.entryconfig(4, state=NORMAL)  # Rotate Image
            self.watermark_menu.entryconfig(0, state=NORMAL)  # Add Watermark

    def add_watermark(self):
        self.watermark_text = simpledialog.askstring("Add Watermark", "Enter watermark text:")
        if self.watermark_text:
            self.apply_watermark()
            self.watermark_menu.entryconfig(0, label="Edit Watermark")
            self.watermark_menu.entryconfig(1, state=NORMAL)
            self.watermark_menu.entryconfig(2, state=NORMAL)

    def edit_watermark(self):
        self.watermark_text = simpledialog.askstring("Edit Watermark", "Edit watermark text:", initialvalue=self.watermark_text)
        if self.watermark_text:
            self.apply_watermark()

    def remove_watermark(self):
        self.image = self.original_image.copy()
        self.watermark_text = ""
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)
        self.watermark_menu.entryconfig(0, label="Add Watermark")
        self.watermark_menu.entryconfig(1, state=DISABLED)
        self.watermark_menu.entryconfig(2, state=DISABLED)

    def apply_watermark(self):
        # Add watermark to image
        self.image = self.original_image.copy()
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((10, 10), self.watermark_text, font=font, fill='black')

        # Update image on canvas
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

    def save_image(self):
        # Open file dialog to save image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def rotate_image(self):
        # Rotate image by 90 degrees
        self.image = self.image.rotate(90, expand=True)
        self.original_image = self.image.copy()

        # Update image on canvas
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

if __name__ == '__main__':
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
