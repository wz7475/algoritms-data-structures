from platform import platform


def read_contents() -> str:
    file_name = (
        "../pan-tadeusz.txt" if "Windows" in platform()
        else "pan-tadeusz-unix.txt")

    with open(file_name, encoding="utf8") as f:
        contents = f.read()

    return contents
