import os
import sys
import argparse

def main(input_data_path,output_data_path):
	comp='bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 \
    		mediapipe/examples/desktop/hand_tracking:hand_tracking_cpu'
	#명령어 컴파일
	cmd='GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_cpu  --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt'
	#미디어 파이프 명령어 저장
	listfile=os.listdir(input_data_path)
	for file in listfile:
    		#해당 디렉토리의 하위 디렉토리 폴더명을 찾음
		word=file+'/'
		fullfilename=os.listdir(input_data_path+word)
		# 하위디렉토리의 모든 비디오들의 이름을 저장
		if not(os.path.isdir(output_data_path+"_"+word)):
			os.mkdir(output_data_path+"_"+word)
		if not(os.path.isdir(output_data_path+word)):
			os.mkdir(output_data_path+word)
		os.system(comp)
		for mp4list in fullfilename:
			inputfilen='   --input_video_path='+input_data_path+word+mp4list
			outputfilen='   --output_video_path='+output_data_path+'_'+word+mp4list
			cmdret=cmd+inputfilen+outputfilen
			os.system(cmdret)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='operating Mediapipe')
	parser.add_argument("--input_data_path",help=" ")
	parser.add_argument("--output_data_path",help=" ")
	args=parser.parse_args()
	input_data_path=args.input_data_path
	output_data_path=args.output_data_path
	#print(input_data_path)
	main(input_data_path,output_data_path)

