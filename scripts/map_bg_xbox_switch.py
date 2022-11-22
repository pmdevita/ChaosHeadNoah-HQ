from print_file_names import get_file_listing
from pathlib import Path

# This was used as a starting point for mapping the Xbox and Switch/Steam bgs. The end result
# still had to be edited since there are some bizarre renames

xbox_path = Path(r"D:\Users\pmdevita\Downloads\Chaos;Head Noah\cg\bg")
switch_path = Path(r"C:\Users\pmdevita\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs\bg")

xbox_files = get_file_listing(xbox_path)
switch_files = get_file_listing(switch_path)

xbox_iter = iter(xbox_files)
switch_iter = iter(switch_files)

xbox_flag = True
switch_flag = True

xbox_advance = True
switch_advance = True

def asdf(files):
    final = set()
    for file in files:
        if file.startswith("bg"):
            final.add(file[:10])
    return final

xbox_set = asdf(xbox_files)
switch_set = asdf(switch_files)

intersection = xbox_set.intersection(switch_set)
diff1 = xbox_set.difference(switch_set)
diff2 = switch_set.difference(xbox_set)

all_files = [[i, 0] for i in intersection] + [[i, -1] for i in diff1] + [[i, 1] for i in diff2]
all_files = sorted(all_files, key=lambda x: x[0])

for file in all_files:
    if file[1] == 0:
        print(file[0])
    elif file[1] == -1:
        print("xbox", file[0])
    elif file[1] == 1:
        print("switch", file[0])


