import os
import pathlib


if __name__ == "__main__":
    """
    Given 2 directory "compare_dir_1" & "compare_dir_2". Suppose you are storing images redundantly in them, 
    but you forgot which one os your main directory since you are managing your images manually.  
    Ideally, I should store everything according to the 3-2-1 rule: 
     - Having 3 different copies
     - Across 2 different types of devices
     - With 1 storage offsite (Not in the same geological location.)
    For this, I should definitely set up a NAS system as well.
    You can also build a NAS with Rasberry as well: https://www.raspberrypi.com/tutorials/nas-box-raspberry-pi-tutorial/
    Or an old Laptop: https://www.youtube.com/watch?v=ZInPE-sG0Ug
    """
    compare_dir_1 = pathlib.Path('C:/move/pictures')
    compare_dir_2 = pathlib.Path('E:/_move/Kepek_videok')
    path_pairs = [(compare_dir_1, compare_dir_2)]

    i = 1
    while True:
        for p1, p2 in path_pairs:
            set_1 = os.listdir(p1)
            set_2 = os.listdir(p2)

            for element in set_1:
                if element not in set_2:
                    print(f'Level_{i}: Could not find "{element}" at {str(p2)}')

            for element in set_2:
                if element not in set_1:
                    print(f'Level_{i}: Could not find "{element}" at {str(p1)}')

            # Get only directory intersections
            path_pairs = [(p1 / element, p2 / element) for element in set(set_1).intersection(set_2)
                          if os.path.isdir(str(p1 / element))]

        if not path_pairs:
            break

        i += 1
