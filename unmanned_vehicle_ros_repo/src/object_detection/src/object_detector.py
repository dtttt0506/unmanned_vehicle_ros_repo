#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        rospy.init_node('object_detector_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)
        self.detection_pub = rospy.Publisher('/object_detections', String, queue_size=10)
        rospy.loginfo("Object Detector Node Initialized.")

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr(e)
            return

        # Simulate object detection (replace with actual ML model inference)
        # For demonstration, let's say we detect a 'car' in the center of the image
        detection_info = "No object detected"
        if np.random.rand() > 0.5: # Simulate detection 50% of the time
            obj_class = "car"
            x_min, y_min, x_max, y_max = 100, 100, 300, 300 # Bounding box coordinates
            detection_info = f"Detected: {obj_class} at [{x_min},{y_min},{x_max},{y_max}]"
            cv2.rectangle(cv_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(cv_image, obj_class, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        self.detection_pub.publish(detection_info)
        # Optionally, publish the image with detections for visualization
        # self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))

        # For demonstration, display the image (will not work in headless environment)
        # cv2.imshow("Image Window", cv_image)
        # cv2.waitKey(1)

if __name__ == '__main__':
    try:
        detector = ObjectDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


