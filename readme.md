<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deepfake Detection Web Application</title>
</head>
<body>

<h1>Deepfake Detection Web Application</h1>

<p>This web application allows users to upload a video, which is then analyzed to detect whether it contains deepfake content. The app processes the video, extracts frames, and uses a pre-trained deep learning model to evaluate each frame's authenticity.</p>
[![Deepfake Detection Demo]
https://img.youtube.com/vi/W8vzLt1McN0/0.jpg

https://youtu.be/W8vzLt1McN0


<h2>Features</h2>
<ul>
    <li>Video upload via a web interface</li>
    <li>Frame extraction from the uploaded video</li>
    <li>Deepfake detection on extracted frames</li>
    <li>Results displayed with confidence scores</li>
</ul>

<h2>Requirements</h2>
<p>To run this application, you'll need the following libraries installed:</p>

<pre><code>opencv-python-headless
numpy
tensorflow
django
</code></pre>

<h2>Installation</h2>

<ol>
    <li><strong>Clone the repository:</strong>

    <pre><code>git clone https://github.com/gitone912/deepfaker_deepfake_detector.git
cd deepfaker_deepfake_detector
    </code></pre></li>

    <li><strong>Create a virtual environment (optional but recommended):</strong>

    <pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
    </code></pre></li>

    <li><strong>Install the required libraries:</strong>

    <pre><code>pip install -r requirements.txt
    </code></pre></li>

    <li><strong>Set up Django:</strong>
    <ul>
        <li>Apply migrations:</li>
        <pre><code>python manage.py migrate
        </code></pre>
        <li>Create a superuser for the admin interface:</li>
        <pre><code>python manage.py createsuperuser
        </code></pre>
    </ul>
    </li>
</ol>

<h2>Usage</h2>

<ol>
    <li><strong>Run the Django development server:</strong>
    <pre><code>python manage.py runserver
    </code></pre></li>

    <li><strong>Open your web browser and navigate to:</strong>
    <pre><code>http://127.0.0.1:8000/
    </code></pre></li>

    <li><strong>Upload a video:</strong>
    <ul>
        <li>Click on upload video to upload a video file.</li>
        <li>The server will process the video, extract frames, and evaluate them using the deepfake detection model.</li>
    </ul></li>

    <li><strong>View the results:</strong>
    <ul>
        <li>The results page will display each frame's evaluation, including the confidence score and the overall prediction for the video.</li>
    </ul></li>
</ol>

<h2>Project Structure</h2>

<ul>
    <li><strong>models/deepfake_detection_model.h5</strong>: The pre-trained deepfake detection model.</li>
    <li><strong>media/</strong>: Directory for storing uploaded videos and extracted frames.</li>
    <li><strong>app_name/</strong>: Replace <code>app_name</code> with your actual Django app name containing:
        <ul>
            <li><code>views.py</code>: Contains the logic for video upload, frame extraction, and evaluation.</li>
            <li><code>forms.py</code>: Contains the form for video upload.</li>
            <li><code>templates/</code>: Directory for HTML templates.</li>
        </ul>
    </li>
</ul>

<h2>Code Overview</h2>
<ul>
    <li><strong>FrameCapture(path)</strong>: Extracts frames from the video located at <code>path</code>.</li>
    <li><strong>evaluate_frames(directory)</strong>: Evaluates extracted frames for deepfake content.</li>
    <li><strong>upload_video(request)</strong>: Handles video upload and initiates the frame extraction and evaluation process.</li>
</ul>

<h2>Notes</h2>
<p>Ensure the pre-trained model <code>deepfake_detection_model.h5</code> is placed in the <code>models</code> directory. The app is configured to delete and recreate the <code>media</code> directory with each new video upload to ensure a clean processing environment.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

<h2>Contact</h2>
<p>For any questions or feedback, please contact Akash Verma on Instagram @frozen_blink.</p>

</body>
</html>
