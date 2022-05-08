import os
import sys
from pathlib import Path

from loguru import logger
from typer import Typer

from . import __version_str__
from .lexer import Lexer
from .parser import Parser
from .utils import read_yml

logger.remove()
logger.add(sys.stderr, level="INFO")

app = Typer()


@app.command()
def version():
    print(__version_str__)


@app.command()
def tokenize(file_path: str):
    with open(file_path, "r") as f:
        input_text = f.read()

    yml_path = os.path.join(Path(__file__).parent, "token.yml")

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(input_text)

    for token in tokens:
        print(token)


@app.command()
def run(file_path: str):
    with open(file_path, "r") as f:
        input_text = f.read()

    yml_path = os.path.join(Path(__file__).parent, "token.yml")

    tokens_dict = read_yml(yml_path)

    lexer = Lexer(tokens_dict).get_lexer()
    tokens = lexer.lex(input_text)

    parser = Parser(list(tokens_dict.keys()))
    parser.parse()

    parser = parser.get_parser()

    parsed = parser.parse(tokens)

    parsed.eval()


if __name__ == "__main__":
    app()
