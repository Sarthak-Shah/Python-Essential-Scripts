import time
from pathlib import Path


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


def main():
    base_dir = Path("data")
    files = [base_dir / f"file{i}.txt" for i in range(1, 4)]

    start = time.time()

    for file in files:
        content = read_file(file)
        print(f"{file.name} has {len(content)} characters")
        time.sleep(1)
        print(content,end="\n\n")

    end = time.time()
    print(f"Total time (sync): {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
