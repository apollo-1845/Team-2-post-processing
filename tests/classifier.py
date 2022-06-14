#!/usr/bin/env python
import os

from classifier.classifier import Classifier
from results.data_point import DataPoint
from misc.serialise_data_points import deserialise_from_file

from tensorflow.keras.models import (
    load_model,
)  # Trained and created separately; load the TF model into the classifier


def get_datapoint(id: int) -> DataPoint:
    # Get image
    data_points = deserialise_from_file(f"./intermediates/full_data.json")
    i = 1
    for point in data_points:
        if i == id:
            return point
        i += 1


def run_test():
    # Load NN model
    model = load_model(os.path.join("data", "classifier", "model"))

    # Create classifier
    print("Getting datapoint...")
    datapoint = get_datapoint(670)  # Falkland Islands
    print("Got datapoint!")
    camera_data = datapoint.get_camera_data()
    channels = camera_data.get_raw_channels()
    classifier = Classifier(
        channels,
    )