#!python3

"""
This script concatenates the list in every json file contained in the input path together in one json file called `_all.json`
so that can be imported in ephios.
"""
import argparse
import json
import re
import sys
from pathlib import Path


TARGET_FILENAME = "_all.json"


def collect(path: Path):
    all_objects = []
    for json_path in sorted(
        [path for path in path.glob("**/*.json") if path.name != TARGET_FILENAME]
    ):
        with open(json_path, "r") as json_file:
            objects = json.load(json_file)
        for obj in objects:
            if obj["uuid"] in [o["uuid"] for o in all_objects]:
                print("ERROR")
                print(f"duplicate object uuid {obj['title']}")
                sys.exit(1)
            all_objects.append(obj)

    with open(path / TARGET_FILENAME, "w") as target_file:
        json.dump(all_objects, target_file, ensure_ascii=False)


def visualize(path):
    with open(path / TARGET_FILENAME, "r") as target_file:
        all_objects = json.load(target_file)

    script = "flowchart LR\n"
    edges = set()
    for obj in all_objects:
        uuid = obj["uuid"]
        script += f'\t{uuid}(["{obj['abbreviation']}"])\n'
        for includes in obj["includes"]:
            edges.add((uuid, includes))
        for included_by in obj["included_by"]:
            edges.add((included_by, uuid))
    for a, b in sorted(edges):
        script += f"\t{a} --> {b}\n"

    with open(path / f"{TARGET_FILENAME}.mermaid", "w") as mermaid_file:
        mermaid_file.write(script)


def main():
    parser = argparse.ArgumentParser(
        description=f"Concatenate lists in every json file contained in the input paths together in one json file called `{TARGET_FILENAME}` "
        "so that it can be imported as a single file."
    )
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "-p", "--paths", nargs="+", type=Path, dest="paths", metavar="PATH"
    )
    input_group.add_argument(
        "-a",
        "--all",
        action="store_true",
        dest="collect_all",
        help="collect from all two-letter subdirectories of the working directory",
    )
    parser.add_argument(
        "-m",
        "--mermaid",
        action="store_true",
        dest="mermaid",
        help="generate mermaid code for the inclusion graph",
    )
    args = parser.parse_args()

    if args.collect_all:
        paths = [
            p
            for p in Path(".").iterdir()
            if p.is_dir() and re.fullmatch(r"\w{2}", p.name)
        ]
    else:
        paths = args.paths
        for path in paths:
            if not path.exists():
                raise FileNotFoundError(f"{path.resolve()!s} does not exist.")

    for path in paths:
        print(f"Collecting '{path!s}': ", end="", flush=True)
        collect(path)
        if args.mermaid:
            visualize(path)
        print("DONE")


if __name__ == "__main__":
    main()
