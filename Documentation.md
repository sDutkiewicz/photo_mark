# Watermark App Documentation

## Introduction

This document provides a detailed overview of the Watermark App, its classes, methods, and functionalities.

## Classes

### WatermarkApp

#### Description:

The primary class representing the Watermark App.

#### Attributes:

- **master**: The main window for the tkinter app.
- **menu**: The main menu of the application.
- **file_menu**: Submenu for file operations (upload, save, rotate).
- **watermark_menu**: Submenu for watermark operations (add, edit, remove).
- **canvas**: Canvas widget to display the image.
- **image**: The currently loaded image.
- **original_image**: Backup of the original image to allow removing watermarks.
- **watermark_text**: The current watermark text.

#### Methods:

- **__init__(self, master)**:
  - **Parameters**: master - the main window for the tkinter app.
  - **Description**: Initializes the WatermarkApp object and sets up the GUI components.

- **upload_image(self)**:
  - **Description**: Opens a file dialog to select an image and displays it on the canvas. Enables the "Save Image," "Rotate Image," and "Add Watermark" options once an image is uploaded.

- **add_watermark(self)**:
  - **Description**: Prompts the user to enter watermark text and applies it to the image. Changes the menu option to "Edit Watermark" and enables the "Edit Watermark" and "Remove Watermark" options.

- **edit_watermark(self)**:
  - **Description**: Prompts the user to edit the current watermark text and applies the updated text to the image.

- **remove_watermark(self)**:
  - **Description**: Restores the image to its original state, removing any applied watermark. Disables the "Edit Watermark" and "Remove Watermark" options.

- **apply_watermark(self)**:
  - **Description**: Adds the current watermark text to the image and updates the canvas.

- **save_image(self)**:
  - **Description**: Opens a file dialog to save the modified image.

- **rotate_image(self)**:
  - **Description**: Rotates the image by 90 degrees and updates the canvas.

## Execution

The app is executed by creating an instance of the `Tk` class (from `tkinter`), initializing the `WatermarkApp` with it, and starting the tkinter main loop.

## Dependencies

- `tkinter`: For the graphical user interface.
- `PIL`: To handle image operations and manipulations.

## Conclusion

This documentation provides a comprehensive understanding of the Watermark App's structure and functionalities. For any additional queries or support, please refer to the official documentation of the utilized libraries.
