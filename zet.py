import os
import datetime


def create_md():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

    uid = current_datetime.strftime("%Y%m%d%H%M%S")

    title = input("Enter the title: ")

    filename = f"{formatted_datetime}.md"

    yaml_metadata = f"""---
uid: {uid}
title: {title}
date: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}
tags:
---

"""

    with open(filename, "w") as file:
        file.write(yaml_metadata)

    print(f"Note saved as '{filename}'.")


if __name__ == "__main__":
    create_md()
