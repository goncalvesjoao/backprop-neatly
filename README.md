# backprop-neatly

This project implements:
- The **Backpropagation** algorithm using a **fixed-topology, fully connected MLP**,
- The **NEAT** algorithm, and
- The **NEAT+Backprop** algorithm, which combines the two previous algorithms.

using NumPy and evaluates their performance, by trying to solve the classical `XOR`, `Circle`, and `Spiral` **binary-classification** problems.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed globally on your system

## Setup

```bash
uv sync
```

The project pins Python 3.14 in `.python-version`. Hydra 1.4 and OmegaConf
2.4 currently use prerelease versions; `uv.lock` records the exact versions.

## Experiments

The `backprop-neatly` command uses Hydra to select an algorithm, dataset, and
seed. It currently prints the configuration only. Training and dataset
generation are not implemented yet.

```bash
uv run backprop-neatly
uv run backprop-neatly algorithm=neat dataset=spiral seed=202
```

Available algorithms are `backprop`, `neat`, and `backprop_neat`. Available
datasets are `xor`, `circle`, and `spiral`. Their configuration files live in
`src/backprop_neatly/conf/`.

Run every combination of algorithms and seeds with a single command:

```bash
uv run backprop-neatly --multirun \
  algorithm=backprop,neat,backprop_neat \
  dataset=xor,circle,spiral \
  seed=101,202,303,404,505
```

This launches 45 configuration checks sequentially. Each single run writes its
configuration snapshot and log under `outputs/`. Sweeps write under `multirun/`,
with a separate directory for each job.

Inspect default configuration without creating a run, or view CLI help:

```bash
uv run backprop-neatly --cfg job
uv run backprop-neatly --help
```

## Development

The project uses:
- [uv](https://docs.astral.sh/uv/) for dependency management
- [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [ty](https://docs.astral.sh/ty/) for static type checking
- [pytest](https://docs.pytest.org/en/stable/) for automated tests

Repository tools are declared in the `dev` dependency group under `pyproject.toml` and installed by `uv sync`.

### Lint

```bash
uv run ruff check .
```

### Format

```bash
uv run ruff format .
```

### Type-check

```bash
uv run ty check
```

### Test

```bash
uv run pytest
```
