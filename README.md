# Sign language recognition with RNN and Mediapipe
Sign language gesture recognition using a reccurent neural network(RNN) with Mediapipe hand tracking.

This project is for academic purpose. Thank you for Google's Mediapipe team :)

## Data Preprocessing with hand tracking(Desktop)
Create training data on Desktop with any input video using [Hand Tracking](https://github.com/google/mediapipe/blob/master/mediapipe/docs/hand_tracking_desktop.md).
* Install Medapipe
```shell
  git clone https://github.com/google/mediapipe.git
```
* Change tflite_tensors_to_landmarks_caculator.cc file in util
```shell
  cd mediapipe/caculators/tflite
```


## prerequisite



