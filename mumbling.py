def accum(str):
    mumble = ""
    for index, char in enumerate(str):
        mumble += char.upper() + (char.lower() * index)
        if index < len(str) - 1:
          mumble += "-"

    return mumble


print(accum("ass"))
