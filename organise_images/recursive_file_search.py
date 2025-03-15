import os

from pathlib import Path


def list_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for name in files:
            file_list.append(name)
    return file_list


def list_all_files(directory):
    return [file.name for file in Path(directory).rglob('*') if file.is_file()]


all_files = list_all_files("C:/_move/_Pictures_and_Videos")
all_files_correct = list_all_files("E:/_move/_Pictures_and_Videos")

# print(set(all_files_correct) - set(all_files))
in_all_files_but_missing_from_all_files_correct = set(all_files) - set(all_files_correct)
print(in_all_files_but_missing_from_all_files_correct)

pass

