import sys

if not "{{ cookiecutter.project_name }}":
    print(
        "The project_name value cannot by empty. Please, provide a meaningful "
        "value when prompted !"
    )
    sys.exit(1)

if " " in "{{ cookiecutter.project_slug }}":
    print(
        "The project_slug value cannot contain spaces. Please, provide a "
        "non-spaced value when prompted !"
    )
    sys.exit(1)
