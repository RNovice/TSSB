def handle_content(status: list, header: list, info: dict) -> str:

    status.append(info["status"])
    header.append(f'{info["symbol"]}{info["header"]}')
    return f'### {info["symbol"]} {info["name"]} {info["status"]}\n> ' + info["content"].replace("\n", " \n> ")