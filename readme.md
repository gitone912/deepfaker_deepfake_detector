# Deepfake Detection Web Application

This web application allows users to upload a video, which is then analyzed to detect whether it contains deepfake content. The app processes the video, extracts frames, and uses a pre-trained deep learning model to evaluate each frame's authenticity.

## Features

- Video upload via a web interface
- Frame extraction from the uploaded video
- Deepfake detection on extracted frames
- Results displayed with confidence scores

## Requirements

To run this application, you'll need the following libraries installed:

```
opencv-python-headless
numpy
tensorflow
django
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gitone912/deepfaker_deepfake_detector.git
   cd deepfaker_deepfake_detector
   ```
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up Django:**

   - Apply migrations:

     ```bash
     python manage.py migrate
     ```
   - Create a superuser for the admin interface:

     ```bash
     python manage.py createsuperuser
     ```

## Usage

1. **Run the Django development server:**

   ```bash
   python manage.py runserver
   ```
2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:8000/
   ```
3. **Upload a video:**

   - Click on upload video to upload a video file.
   - The server will process the video, extract frames, and evaluate them using the deepfake detection model.
4. **View the results:**

   - The results page will display each frame's evaluation, including the confidence score and the overall prediction for the video.

## Project Structure

- **models/deepfake_detection_model.h5**: The pre-trained deepfake detection model.
- **media/**: Directory for storing uploaded videos and extracted frames.
- **app_name/**: Replace `app_name` with your actual Django app name containing:
  - `views.py`: Contains the logic for video upload, frame extraction, and evaluation.
  - `forms.py`: Contains the form for video upload.
  - `templates/`: Directory for HTML templates.

## Code Overview

- **FrameCapture(path)**: Extracts frames from the video located at `path`.
- **evaluate_frames(directory)**: Evaluates extracted frames for deepfake content.
- **upload_video(request)**: Handles video upload and initiates the frame extraction and evaluation process.

## Notes

- Ensure the pre-trained model `deepfake_detection_model.h5` is placed in the `models` directory.
- The app is configured to delete and recreate the `media` directory with each new video upload to ensure a clean processing environment.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact  akash verma  on my insta @frozen_blink.
