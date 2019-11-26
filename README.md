# Sign language recognition with RNN and Mediapipe
Sign language gesture recognition using a reccurent neural network(RNN) with Mediapipe hand tracking. 

This project is for academic purpose. Thank you for Google's Mediapipe team :)

## Data Preprocessing with hand tracking(Desktop)
Create training data on Desktop with input video using [Hand Tracking](https://github.com/google/mediapipe/blob/master/mediapipe/docs/hand_tracking_mobile_gpu.md).
Gesture recognition with deep learning model can be done with only **42 hand landmarks** RNN training per frame.

**CUSTOMIZE:**
- Use video input instead of Webcam on Desktop to train with video data
- Extract hand landmarks for every frame per one word and make it into one txt file

### 1. Set up Hand Tracking framework
* Install Medapipe
```shell
  git clone https://github.com/google/mediapipe.git
```
See the rest of installation documents [here](https://mediapipe.readthedocs.io/en/latest/install.html).
* Change **tflite_tensors_to_landmarks_caculator.cc** file
```shell
  cd mediapipe/mediapipe/caculators/tflite
  rm tflite_tensors_to_landmarks_caculator.cc
```
to our new tflite_tensors_to_landmarks_caculator.cc file in the modified_mediapipe folder.

* Change **demo_run_graph_main.cc** file 
```shell
  cd mediapipe/mediapipe/examples/desktop
  rm demo_run_graph_main.cc
```
to our new demo_run_graph_main.cc file in the modified_mediapipe folder.

### 2. Create you own training data
Make **train_videos** and **test_videos** for each sign language word in one folder. Copy **build.by** file in util folder to your mediapipe directory.
* Usage

To make mp4 file and txt file with mediapipe automatically, run
```shell
  python build.py --input_data_path=[INPUT_PATH] --output_data_path=[OUTPUT_PATH]
```
inside mediapipe directory.

Change INPUT_PATH, OUTPUT_PATH to your own folder directory path. INPUT_PATH is path to your input videos. OUTPUT_PATH is where all the hand-tracked mp4 files and txt files of 42 landmarks will be saved.

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
OUTPUT_PATH is initially empty directory and when build is done, Mp4 and txt files will be extracted to your own folder path. (DO NOT use space bar or '_' to your folder path and video name ex) Apple_pie (X))

* On training data
```shell
  python make_pickle.py --input_data_path=[INPUT_PATH] --output_file_path=[OUTPUT_FILE]
```

INPUT_PATH is path where all the extracted txt files are saved. This will create file `train_data.pkl` inside OUTPUT_FILE path.

### 3. Train RNN model

* Train
```shell
  python LSTM.py --input_file=[PKL_FILE]
```
Add path to preprocessed pkl file into PKL_FILE.


앞으로 할일: 평가랑 학습 분리, LSTM에 레이어 더 추가, 옵션 구현, 단어 분절 방법 찾기, 가변길이 처리, train/test 








