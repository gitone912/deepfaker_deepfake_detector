import os
import shutil
import cv2
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import VideoUploadForm
from tensorflow.keras.preprocessing import image 

# Load the model once when the server starts
model = tf.keras.models.load_model('models/deepfake_detection_model.h5')

def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1

    frames_dir = os.path.join(settings.MEDIA_ROOT, 'frames')
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    while success:
        success, img = vidObj.read()
        if not success:
            break
        if count % 20 == 0:
            cv2.imwrite(os.path.join(frames_dir, f"frame{count}.jpg"), img)
        count += 1


def evaluate_frames(directory):
    total_confidence = 0
    num_frames = 0
    results = []

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            img_path = os.path.join(directory, filename)
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            confidence = model.predict(img_array)[0][0]
            total_confidence += confidence
            num_frames += 1

            if confidence >= 0.5:
                results.append((filename, "Fake", confidence))
            else:
                results.append((filename, "Real", confidence))

    if num_frames > 0:
        average_confidence = total_confidence / num_frames
        overall_prediction = "The video is predicted as a deepfake." if average_confidence >= 0.5 else "The video is predicted as real."
    else:
        average_confidence = 0
        overall_prediction = "No frames found."

    return results, average_confidence, overall_prediction

def upload_video(request):
    media_dir = settings.MEDIA_ROOT

    # Check if the media directory exists
    if os.path.exists(media_dir):
        # Delete the media directory and all its contents
        shutil.rmtree(media_dir)

    # Create the media directory again
    os.makedirs(media_dir)
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video']
            fs = FileSystemStorage()
            video_path = fs.save(video.name, video)
            video_full_path = os.path.join(settings.MEDIA_ROOT, video_path)

            FrameCapture(video_full_path)

            frames_dir = os.path.join(settings.MEDIA_ROOT, 'frames')
            results, avg_confidence, overall_prediction = evaluate_frames(frames_dir)

            return render(request, 'results.html', {
                'results': results,
                'average_confidence': avg_confidence,
                'overall_prediction': overall_prediction
            })
    else:
        form = VideoUploadForm()
    return render(request, 'landing_page.html', {'form': form})
