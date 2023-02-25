from pathlib import Path

file = Path("../mapping/CRI File Tools c0data.csv")
lines = []
with open(file) as f:
    for i, line in enumerate(f.readlines()):
        parts = line.split(",")
        try:
            assert len(parts) == 4
        except:
            print(parts, line)
        parts[2] = str(i)
        lines.append(",".join(parts))

with open(file.with_stem(file.stem + "fixed"), "w") as f:
    f.writelines(lines)


