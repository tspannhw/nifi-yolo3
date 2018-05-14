cd /Volumes/seagate/models/darknet-master
/Volumes/seagate/models/darknet-master/darknet detect /Volumes/seagate/models/darknet-master/cfg/yolov3.cfg /Volumes/seagate/models/darknet-master/cfg/yolov3.weights /Volumes/seagate/models/darknet-master/`python /Volumes/seagate/models/darknet-master/capture.py`
cp predictions.png /Volumes/seagate/models/darknet-master/images/predictions.`date +%Y%m%d%H%M%S`.png
