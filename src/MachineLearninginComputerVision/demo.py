#! /usr/bin/env python
# ================================================================
#   Copyright (C) 2018 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : video_demo.py
#   Author      : YunYang1994
#   Created date: 2018-11-30 15:56:37
#   Description :
#
# ================================================================

import os
import os.path as osp

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

import MachineLearninginComputerVision.core.utils as utils

# import time


direct_path = osp.abspath(osp.dirname(__file__)).replace(os.sep, "/")


def main(video_path=direct_path + "/sample/road.mp4", show=True):
    return_elements = ["input/input_data:0", "pred_sbbox/concat_2:0", "pred_lbbox/concat_2:0"]
    pb_file = direct_path + "/model/yolov3_nano_416.pb"
    # video_path      = 0
    num_classes = 20
    input_size = 416
    graph = tf.Graph()
    return_tensors = utils.read_pb_return_tensors(graph, pb_file, return_elements)

    print("input.name =", return_tensors[0].name)  # import/input/input_data:0
    print("output1.name =", return_tensors[1].name)  # import/pred_sbbox/concat_2:0
    print("output2.name =", return_tensors[2].name)  # import/pred_lbbox/concat_2:0

    with tf.compat.v1.Session(graph=graph) as sess:
        vid = cv2.VideoCapture(video_path)
        while True:
            return_value, frame = vid.read()
            if return_value:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
            else:
                raise ValueError("No image!")
            frame_size = frame.shape[:2]
            image_data = utils.image_preporcess(np.copy(frame), [input_size, input_size])
            image_data = image_data[np.newaxis, ...]
            # prev_time = time.time()

            pred_sbbox, pred_lbbox = sess.run(
                [return_tensors[1], return_tensors[2]], feed_dict={return_tensors[0]: image_data}
            )

            pred_bbox = np.concatenate(
                [
                    np.reshape(pred_sbbox, (-1, 5 + num_classes)),
                    np.reshape(pred_lbbox, (-1, 5 + num_classes)),
                ],
                axis=0,
            )

            bboxes = utils.postprocess_boxes(pred_bbox, frame_size, input_size, 0.3)
            bboxes = utils.nms(bboxes, 0.45, method="nms")
            image = utils.draw_bbox(frame, bboxes)

            # curr_time = time.time()
            # exec_time = curr_time - prev_time
            result = np.asarray(image)
            # info = "time: %.2f ms" % (1000 * exec_time)
            if show:
                cv2.namedWindow("result", cv2.WINDOW_NORMAL)
                result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                result_s = cv2.resize(result, (1920, 1080))
                cv2.imshow("result", result_s)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            return result
