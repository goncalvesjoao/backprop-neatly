"""Hydra entry point for configuring experiments."""

import logging

import hydra
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


@hydra.main(config_path="conf", config_name="config")
def main(config: DictConfig) -> None:
    """Print the experiment configuration until training is implemented."""
    logger.info("Configuration check only; training is not implemented yet.")
    logger.info("\n%s", OmegaConf.to_yaml(config, resolve=True))


if __name__ == "__main__":
    main()
