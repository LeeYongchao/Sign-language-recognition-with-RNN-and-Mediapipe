# Sign language recognition with RNN and Mediapipe
Sign language gesture recognition using a reccurent neural network(RNN) with Mediapipe hand tracking. 

This project is for academic purpose. Thank you for Google's Mediapipe team :)

## Data Preprocessing with hand tracking(Desktop)
Create training data on Desktop with input video using [Hand Tracking](https://github.com/google/mediapipe/blob/master/mediapipe/docs/hand_tracking_mobile_gpu.md).
Gesture recognition with deep learning model can be done with only 42 hand landmarks rather than OpenCV approach.

**CUSTOMIZE:**
- Use video input instead of Webcam on Desktop to train with video data
- Extract hand landmarks for every frame per one word and make it into one txt file

### 1. Set up Hand Tracking framework
* Install Medapipe
```shell
  git clone https://github.com/google/mediapipe.git
```
See the rest of installation documents [here](https://mediapipe.readthedocs.io/en/latest/install.html) 
* Change tflite_tensors_to_landmarks_caculator.cc file in util 
```shell
  cd mediapipe/mediapipe/caculators/tflite
  rm tflite_tensors_to_landmarks_caculator.cc
```
and add our new **tflite_tensors_to_landmarks_caculator.cc** file in the util folder.

### 2. Create you own training data
Make **train_videos** and **test_videos** for each sign language word in one folder. INPUT_PATH is path to your input video and OUTPUT_PATH is where mp4 file with hand tracking will be saved. All the txt files of 42 landmarks(21 * (x, y)) in each frame for one word will be saved in OUTPUT_TEXT_PATH. 

* Usage
To make mp4 file and txt file with mediapipe automatically, run
```shell
  python get_text.py --input_data_path=[INPUT_PATH] --output_data_path=[OUTPUT_PATH] --output_file_path=[OUTPUT_TEXT_PATH]
```
Change INPUT_PATH, OUTPUT_PATH, OUTPUT_TEXT_PATH to your own folder directory path.

For example:
```shell
  input_videos
├── Apple
│   ├── IMG_2733.MOV
│   ├── IMG_2734.MOV
│   ├── IMG_2735.MOV
│   └── IMG_2736.MOV
├── Drink
│   ├── IMG_2631.MOV
│   ├── IMG_2632.MOV
│   ├── IMG_2633.MOV
│   └── IMG_2634.MOV
└── Hello
    ├── IMG_2472.MOV
    ├── IMG_2473.MOV
    ├── IMG_2474.MOV
    └── IMG_2475.MOV
    ...
```
Mp4 and txt files will be extracted to your own folder path.

* On training data
```shell
  python get_data.py --input_data_path=[INPUT_PATH] --output_file_path=[OUTPUT_FILE]
```
This will create file `train_data.pkl`
(아직 옵션은 구현 안함)

### 3. Train RNN model

* Train
```shell
  python model.py [--input_file=PKL_FILE]
```
(아직 옵션 구현 안함)


앞으로 할일: 평가랑 학습 분리, LSTM에 레이어 더 추가, 옵션 구현, 단어 분절 방법 찾기, 가변길이 처리, train/test 








