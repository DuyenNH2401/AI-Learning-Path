##English Ver

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
```

##Vietnamese Ver

# 🏞️ Thay thế Nền ảnh bằng OpenCV (Image Background Replacement)

Đây là một dự án Python đơn giản sử dụng thư viện **OpenCV** và **NumPy** để thực hiện kỹ thuật thay thế nền ảnh, tương tự như kỹ thuật "phông xanh" (green screen).

Dự án hoạt động bằng cách so sánh ảnh có đối tượng trên nền xanh với ảnh chỉ có nền xanh để tạo ra một "mặt nạ" (mask) cho đối tượng. Sau đó, mặt nạ này được dùng để tách đối tượng và ghép vào một ảnh nền mới.

## 🖼️ Kết quả Demo

| Ảnh đối tượng | Nền mới | Kết quả cuối cùng |
| :---: | :---: | :---: |
| ![Object Image](Object.png) | ![New Background](NewBackground.jpg) | ![Final Result](result.png) |
*(Lưu ý: Bạn cần có các file `Object.png`, `NewBackground.jpg`, và `result.png` trong repo để hình ảnh hiển thị)*

## ✨ Chức năng chính

-   Tách đối tượng khỏi nền đơn sắc (trong ví dụ này là màu xanh lá).
-   Thay thế nền cũ bằng một ảnh nền hoàn toàn mới.
-   Sử dụng phép trừ ảnh (image subtraction) để xác định vị trí của đối tượng.

## 🛠️ Yêu cầu cài đặt

Để chạy được dự án này, bạn cần cài đặt các thư viện cần thiết.

```bash
pip install opencv-python numpy
