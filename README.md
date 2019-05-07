# PH235
Repository for final project: Kalman filter for tracking objects

Required openCv installation. I followed this link for the installation on Mac OS https://medium.com/@nuwanprabhath/installing-opencv-in-macos-high-sierra-for-python-3-89c79f0a246a.

mouse2.py estimates the mouse position when subjected to Gaussian noise

The mp4 video shows a demo

object_tracking3.py takes as optional input --video video_name.mp4 --tracker tracker_type (kcf, csrt, boosting, mil, tld, medianflow, mosse)

If the video is not specified it takes as input the camera feed. Hover over the video frame, when you find the right frame press 's' and drag a box around the object to be tracked and then press 'enter'. 


