import os
import os.path as osp

import cv2
import numpy as np
import pytest

from MachineLearninginComputerVision import demo

direct_path = osp.abspath(osp.dirname(__file__)).replace(os.sep, "/")


def test_regression():
    true = cv2.imread(direct_path + "/samples/result.png")
    pred = demo.main(image_path=direct_path + "/samples/source.jpg", show=False)

    assert true.shape == pred.shape

    assert np.array_equal(true, pred)


@pytest.mark.parametrize("image_type", ["large.jpg", "small.jpg"])
def test_correct_sizes(image_type):
    demo.main(direct_path + "/samples/" + image_type, show=False)


def test_same_result():
    first = demo.main(image_path=direct_path + "/samples/source.jpg", show=False)
    second = demo.main(image_path=direct_path + "/samples/source.jpg", show=False)

    assert np.array_equal(first, second)
