from misc.serialise_data_points import deserialise_from_prompt, serialise_from_prompt

if __name__ == "__main__":
    data_points = deserialise_from_prompt()
    new_data_points = []
    for point in data_points:
        # Get NDVI - lazy evaluation
        print("Land type:", point.get_land_cover())
        print("NDVI:", point.get_mean_ndvi(), "Expected", point.get_expected_ndvi())
        new_data_points.append(point)

    serialise_from_prompt(new_data_points, "ndvi_processed")