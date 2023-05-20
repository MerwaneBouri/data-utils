import json
from shapely.geometry import shape, mapping
from pathlib import Path

from tdd.remove_overlap import remove_orverlap

with (Path(__file__).parent / "data" / "overlap" / "input.json").open("r") as f:
    input_data = json.load(f)

with (Path(__file__).parent / "data" / "overlap" / "expected.json").open("r") as f:
    expected_data = json.load(f)


def test_remove_orverlap():
    poly1 = shape(input_data["features"][0]["geometry"])
    poly2 = shape(input_data["features"][1]["geometry"])

    res_poly_1, res_poly_2 = remove_orverlap(poly1, poly2)
    assert res_poly_1.equals(shape(expected_data["features"][0]["geometry"]))
    assert res_poly_2.equals(shape(expected_data["features"][1]["geometry"]))


if __name__ == "__main__":
    print(input_data)
    print(expected_data)