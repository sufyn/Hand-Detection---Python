# Hand Tracking Project

This project utilizes OpenCV and MediaPipe to perform real-time hand tracking using a webcam. The application detects and visualizes hand landmarks on the captured video feed. It uses MediaPipe's Hand module to detect and track hands with high accuracy.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- OpenCV
- MediaPipe

You can install the required dependencies using the following commands:

```bash
pip install opencv-python mediapipe
```

## Project Description

The project captures a video feed from the webcam, processes the video frames using MediaPipe's `Hands` solution, and identifies the hand landmarks in real-time. These landmarks are visualized using OpenCV, with the connections between the hand landmarks drawn on the screen.

### Features

- Real-time hand tracking using the webcam
- Drawing landmarks and connections on the detected hands
- Option to exit the program by pressing the "q" key

## Usage

1. Clone the repository or download the code.
2. Run the Python script to start the hand tracking application.

```bash
python hand_tracking.py
```

3. The application will open a window displaying the webcam feed with detected hand landmarks. Press 'q' to close the window and stop the application.

## Code Explanation

- **cv2.VideoCapture(0)**: Captures video from the webcam.
- **mp_hands.Hands**: MediaPipe's solution for detecting hands in real-time. It takes parameters such as `min_detection_confidence` and `min_tracking_confidence` to set the thresholds for detection and tracking accuracy.
- **mp_drawings.draw_landmarks()**: Draws the detected landmarks and their connections on the frame.
- **Flip and Color Conversion**: The video frame is converted to RGB format, flipped horizontally (for a mirror effect), and then processed to detect hands.
- **Displaying Results**: The results are drawn on the frame, and the updated frame is displayed using OpenCV.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- [OpenCV](https://opencv.org/) for computer vision tasks.
- [MediaPipe](https://mediapipe.dev/) for hand tracking solution.
```
