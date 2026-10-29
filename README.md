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

## Development

The project uses [uv](https://docs.astral.sh/uv/) for dependency management,
[Ruff](https://docs.astral.sh/ruff/) for linting and formatting,
[ty](https://docs.astral.sh/ty/) for static type checking, and
[pytest](https://docs.pytest.org/en/stable/) for automated tests. Repository
settings configure the same tools in **Zed** and **VS Code**.

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
