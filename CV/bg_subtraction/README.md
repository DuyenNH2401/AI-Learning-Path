# 🏞️ Image Background Replacement using OpenCV

This is a simple Python project that uses the **OpenCV** and **NumPy** libraries to perform background replacement, similar to a "green screen" or "chroma key" effect.

The project works by comparing an image of an object on a green background with an image of just the green background. This comparison creates a "mask" for the object. This mask is then used to isolate the object and place it onto a new background image.

## 🖼️ Demo

| Object Image | New Background | Final Result |
| :---: | :---: | :---: |
| ![Object Image](Object.png) | ![New Background](NewBackground.jpg) | ![Final Result](result.png) |
*(Note: You need the `Object.png`, `NewBackground.jpg`, and `result.png` files in your repository for the images to display correctly.)*

## ✨ Key Features

-   Separates an object from a solid color background (green in this example).
-   Replaces the original background with a new image.
-   Uses image subtraction to create a mask for the object.

## 🛠️ Requirements

To run this project, you need to install the required libraries.

```bash
pip install opencv-python numpy
