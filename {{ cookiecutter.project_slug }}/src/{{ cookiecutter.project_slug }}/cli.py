import typer

app = typer.Typer()


@app.command()
def main():
    name = '{{ cookiecutter.project_slug }}'
    print(f"Hello {name}!")


if __name__ == "__main__":
    app()
