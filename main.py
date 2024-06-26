from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Watermark App")

        # Create buttons
        self.upload_button = Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.add_button = Button(master, text="Add Watermark", command=self.add_watermark, state=DISABLED)
        self.add_button.pack()

        self.save_button = Button(master, text="Save Image", command=self.save_image, state=DISABLED)
        self.save_button.pack()

        self.rotate_button = Button(master, text="Rotate Image", command=self.rotate_image, state=DISABLED)
        self.rotate_button.pack()

        # Create canvas for displaying image
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()

        # Create watermark entry field
        self.watermark_entry = Entry(master)
        self.watermark_entry.pack()

    def upload_image(self):
        # Open file dialog to select image
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)

            # Resize image if necessary
            if self.image.size[0] > 400 or self.image.size[1] > 400:
                self.image.thumbnail((400, 400))

            # Display image on canvas
            self.photo_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

            # Enable buttons
            self.add_button.config(state=NORMAL)
            self.save_button.config(state=NORMAL)
            self.rotate_button.config(state=NORMAL)

    def add_watermark(self):
        # Get watermark text from entry field
        watermark_text = self.watermark_entry.get()

        # Add watermark to image
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 36)
        draw.text((10, 10), watermark_text, font=font, fill='black')

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

        # Update image on canvas
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)

if __name__ == '__main__':
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
