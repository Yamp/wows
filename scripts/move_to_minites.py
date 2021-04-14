import shutil
from pathlib import Path


def main():
    data_path = (Path(__file__).parent.parent / 'data' / 'usa' / 'minutes1').resolve().absolute()

    for f in data_path.iterdir():
        name = f.name
        if not name.endswith('_.parquet'):
            print(f'Skipping {name}')
        else:
            new_path = data_path / (name.removesuffix('_.parquet') + '.parquet')
            shutil.move(f, new_path)


if __name__ == "__main__":
    main()
