import logging
import os

import click
from speed import SpeedtestLogger


@click.command()
@click.option("-n", "--ntests", default=1, help="Number of tests.")
@click.option("-i", "--interval", default=1, help="Interval between tests.")
@click.option("-o", "--out", default="speed_test_results.csv", help="Output file.")
@click.option("-l", "--logging_level", default=20, help="Logging level.")
def run(ntests, interval, out, logging_level):

    # Set logging level
    logging.getLogger().setLevel(logging_level)

    SpeedtestLogger(out).log_tests(ntests)


if __name__ == "__main__":
    run()
