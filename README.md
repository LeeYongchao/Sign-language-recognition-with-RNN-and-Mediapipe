# Sign language recognition with RNN and Mediapipe
Sign language gesture recognition using a reccurent neural network(RNN) with Mediapipe hand tracking.

This project is for academic purpose. Thank you for Google's Mediapipe team :)

## Data Preprocessing with hand tracking(Desktop)
Create training data on Desktop with input video using [Hand Tracking](https://github.com/google/mediapipe/blob/master/mediapipe/docs/hand_tracking_mobile_gpu.md)

**CUSTOMIZE:**
- Use video input instead of Webcam on Desktop to train with video data
- Extract hand landmarks for every frame per one word and make it into one txt file

* Install Medapipe
```shell
  git clone https://github.com/google/mediapipe.git
```
See the rest of installation documents [here](https://mediapipe.readthedocs.io/en/latest/install.html) 
* Change tflite_tensors_to_landmarks_caculator.cc file in util 
```shell
  cd mediapipe/caculators/tflite
```




