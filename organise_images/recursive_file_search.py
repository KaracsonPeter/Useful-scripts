import os

from pathlib import Path


"""
This script recursively finds each file in the provided (and hardcoded) directory trees.
Also tells what is missing from each others' location. 
E.g.:
a_location:
- alma.txt
- banan.txt

b_location:
- banan.txt
- citrom.txt

present_in_location_a_missing_form_b = [alma.txt]
present_in_location_b_missing_form_a = [citrom.txt]
"""


def list_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for name in files:
            file_list.append(name)
    return file_list


def list_all_files(directory):
    return [file.name for file in Path(directory).rglob('*') if file.is_file()]


a_location = list_all_files("C:/_move/_Pictures_and_Videos")
b_location = list_all_files("E:/_move/_Pictures_and_Videos")

present_in_location_a_missing_form_b = set(a_location) - set(b_location)
present_in_location_b_missing_form_a = set(b_location) - set(a_location)

breakpoint()
