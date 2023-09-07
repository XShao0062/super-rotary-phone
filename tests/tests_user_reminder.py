import re
#from mymodule.cli_coordinate_calculator import *
from astropy.coordinates import Angle
#def test_module_import():
 #   try:
        #from mymodule import coord_cal

  #  except Exception as e:
   #     raise AssertionError("Failed to import mymodule")
   # return



def test_get_user_input():
    from mymodule import cli_coordinate_calculator

    if len(reminder) > 8:
        pattern = r'(\d+h\d+m\d+s/\d+d\d+m\d+\.\d+s)'
    else:
        pattern = r'(\d{1,2}[:\s]\d{1,2}[:\s]\d{1,2})'

    matches = re.findall(pattern, reminder)
    match_count = len(matches)

    assert match_count == 1


def test_degree_cal():
# Test cases
    from mymodule import cli_coordinate_calculator
    test_cases = [
        {'input_ra': '12h2m30.5s', 'input_dec': '12d20m30.3s', 'expected_ra': 180.6270833333333, 'expected_dec': 12.341750000000001},
        # Add more test cases as needed
    ]

    # Iterate through the test cases
    for test_case in test_cases:
        ra_degrees, dec_degrees = degree_cal(test_case['input_ra'], test_case['input_dec'])
        try:
            assert ra_degrees == test_case['expected_ra'], f"RA: {ra_degrees}, expected: {test_case['expected_ra']}"
            assert dec_degrees == test_case['expected_dec'], f"Dec: {dec_degrees}, expected: {test_case['expected_dec']}"
        except AssertionError as e:
            print(f"Test case failed: {e}")
        else:
            print("Test case passed")

if __name__ == '__main__':
    test_degree_cal()
