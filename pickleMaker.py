import os
import cv2
import logging
import json
import pickle
import gzip

path_scripts = "job_scripts/"
scriptFiles = []
taskDict = {}
for (dir_path, dir_names, file_names) in os.walk(path_scripts):
    scriptFiles = scriptFiles+file_names
for file in scriptFiles:
    if '.json' in file:
        script_path = path_scripts + file
        with open(script_path, 'r') as f:
            try:
                taskDict[file[:-5]] = json.load(f)
            except ValueError:
                logging.error("Json Script文件出错！")

path_crop = "crop/"
cropFiles = []
buttonImgDict = {}
for (dir_path, dir_names, file_names) in os.walk(path_crop):
    cropFiles = cropFiles+file_names
for file in cropFiles:
    if '.png' in file:
        template_path = path_crop+file.split("-")[0]+'/'+file
        buttonImgDict[file[:-4]] = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)

# Export data to a file
with gzip.open('corp.pkl.gz', 'wb') as f:
    pickle.dump(buttonImgDict, f)
with gzip.open('task.pkl.gz', 'wb') as f:
    pickle.dump(taskDict, f)