from pathlib import Path

PROJECT_DIRECTORY = Path('.').parent


if __name__ == '__main__':
    if '{{ cookiecutter.command_line_interface|lower }}' == "n":
        cli_file = PROJECT_DIRECTORY / '{{ cookiecutter.project_slug }}' / 'src' / '{{ cookiecutter.project_slug }}' / 'cli.py'
        cli_file.unlink()