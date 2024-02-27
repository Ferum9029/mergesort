def console_output(data: list) -> None:
    print(data)


def file_output(data: list, filename: str) -> None:
    with open(filename, "w") as f:
        f.write(str(data))
