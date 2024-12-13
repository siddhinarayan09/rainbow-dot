# Color Recognition Application with OpenCV and Tkinter

This project is a real-time color recognition application that uses OpenCV for video processing and Tkinter for the graphical user interface. Users can capture live video, identify colors by clicking on points in the feed, and highlight matching color regions dynamically.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Output](#output)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## Overview

The Color Recognition Application allows users to:
- Capture and display live video from a webcam.
- Recognize BGR and HSV color values of a clicked point in the video feed.
- Highlight matching contours in the frame dynamically.

This tool is useful for applications in design, art, and industrial quality control.

---

## Features

- **Real-time Video Feed**: Captures live video from the webcam.
- **Color Detection**: Identifies and displays BGR and HSV values of clicked points in the video feed.
- **Contour Highlighting**: Highlights areas in the frame matching the selected color.
- **Interactive GUI**: Intuitive interface using Tkinter for seamless interaction.

---

## Technologies Used

- **Python**: Core programming language.
- **OpenCV**: For video capture, color detection, and contour highlighting.
- **Tkinter**: For graphical user interface design.
- **NumPy**: For numerical computations and data manipulation.
- **Pillow**: For handling images in the Tkinter canvas.

---

## How It Works

1. The application opens a live video feed using OpenCV.
2. Users can click on any point in the video frame to capture the color at that point.
3. The selected color's BGR and HSV values are displayed.
4. Contours matching the selected color are highlighted in the video frame using dynamic masking.

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/color-recognition-app.git
2. **Navigate to the project directory**:
     ```bash
     cd color-recognition-app
3. **Install required dependencies**:
     ```bash
     pip install -r requirements.txt
4. **Run the application:**
     ```bash
     python app.py

---

### Usage

Run the application script.
A Tkinter window will display the live video feed.
Click on any point in the video feed to identify its color.
Observe the BGR and HSV values displayed in the GUI.
Matching contours in the frame are dynamically highlighted.

---

### Output

The application highlights areas in the video feed that match the selected color and provides the following:

BGR and HSV values of the clicked point.
Rectangles around matching contours in the frame.

---

### Future Enhancements

Add functionality to save selected colors to a database for later use.
Integrate Flask for a web-based interface.
Include color palettes for predefined selections.
Enable multi-color detection and tracking.

---

### Acknowledgments

Special thanks to:

The Python and OpenCV documentation for their extensive resources.
Open-source contributors for their valuable tools and libraries.
