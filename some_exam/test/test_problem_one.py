from ..problem_one import ProblemOne
import json
import pytest
import os
cwd = os.path.dirname(os.path.realpath(__file__))
malformed_json_path = f"{cwd}/problem_one.json"
valid_json_path = f"{cwd}/problem_one_valid.json"


@pytest.fixture
def get_json():
    json_dict = {}
    with open(malformed_json_path) as malformed_json_file:
        json_dict['bad'] = json.load(malformed_json_file)
        malformed_json_file.close()
    with open(valid_json_path) as valid_json_file:
        json_dict['good'] = json.load(valid_json_file)
        valid_json_file.close()
    return json_dict


@pytest.fixture
def setup_object():
    problem_one_inst = ProblemOne()
    return problem_one_inst


def test_no_code(get_json, setup_object):
    assert setup_object.transform_me(get_json['bad']) is not False


def test_is_equal(get_json, setup_object):
    assert setup_object.transform_me(get_json['bad']) == get_json['good']