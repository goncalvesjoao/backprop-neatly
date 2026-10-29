"""Check the installed entry point and Hydra's persisted sweep configuration."""

import subprocess
import sys
from pathlib import Path

from omegaconf import OmegaConf


def test_multirun_saves_each_configuration(tmp_path: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "backprop_neatly.experiment",
            "--multirun",
            "algorithm=backprop,neat,backprop_neat",
            "dataset=spiral",
            "seed=101,202",
            f"hydra.sweep.dir={tmp_path}",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )

    configs = [
        OmegaConf.load(path) for path in sorted(tmp_path.glob("*/.hydra/config.yaml"))
    ]
    assert len(configs) == 6
    assert {(cfg.algorithm.name, cfg.seed) for cfg in configs} == {
        (algorithm, seed)
        for algorithm in ("backprop", "neat", "backprop_neat")
        for seed in (101, 202)
    }
    assert all(cfg.dataset.name == "spiral" for cfg in configs)
    assert "training is not implemented yet" in result.stdout
