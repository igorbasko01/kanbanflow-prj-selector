"""Console script for kanbanflow_prj_selector."""
import sys
import click

from .kanbanflow_prj_selector import start


@click.command()
@click.option('-f', '--board-token-path', help='Input file with board tokens to fetch', required=True)
def main(board_token_path):
    """Console script for kanbanflow_prj_selector."""
    start(board_token_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
