# jetbot_search

Please pay attention that you give the JetBot enough place to move around and be sure there are no dangerous situations around, the obstacle avoidance is not perfect and the code is not working live yet.

With this software, the jetbot should be able to search inside a room for a certain object of the [COCO dataset](https://cocodataset.org/#home).

Whatsoever, the computing power of the jetbot is to little that the jetbot can really drive on its own. Due to the little computing power, the object detection/ obstacle avoidance is not fast enough for the given resolution/ velocity of the robot.

To be able to use it, make sure you download all the necessary software for the JetBot and the following models and add them in the same folder as the [main file](https://github.com/nechl/jetbot_search/blob/main/stable_detection.ipynb) :
> [Collision avoidance](https://drive.google.com/file/d/1UsRax8bR3R-e-0-80KfH2zAt-IyRPtnW/view)

> [COCO Dataset/SSD MobileNet V2](https://drive.google.com/file/d/1KjlDMRD8uhgQmQK-nC2CZGHFTbq4qQQH/view)

Based on the [NVIDIA AI IOT Jetbot Notebooks](https://github.com/NVIDIA-AI-IOT/jetbot)

Improvements are being made in the Search algorithm and the computing power usage
