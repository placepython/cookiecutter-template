from pathlib import Path
import secrets


def set_flag(
    file_path: Path | str, flag: str, length: int = 64, value: str = None
) -> str:
    """Replace a flag by a value in a file identified by the file_path Path."""
    if isinstance(file_path, str):
        file_path = Path(file_path).resolve()

    if value is None:
        value = secrets.token_urlsafe(length)

    with file_path.open("r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value
