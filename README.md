# ephios-qualification-fixtures

Contains fixtures of commonly used qualifications for ephios.

## Building

For every language, we have a json file per qualification category.
Use `python collect.py --all` to unify them in a single `_all.json` file that can be used
in the qualification importer in ephios.

## Visualizing

Use the `--visualize` flag with the collect script to generate 
mermaid code visualizing the inclusions in every `_all.json`.

```bash
python collect.py --all --visualize
```

The code can be rendered to an image using mermaid-cli, e.g.:
```bash
mmdc -i de/_all.json.mermaid -o de/_all.svg
```

<img src="https://raw.githubusercontent.com/ephios-dev/ephios-qualification-fixtures/refs/heads/main/de/_all.svg" alt="graph visualization of german qualification fixtures">
