import ipdb

def oxford_comma(items):
    if len(items) == 2:
        return " and ".join(items)
    elif len(items) > 2:
        last_item = items[-1]
        items[-1] = "and " + last_item
        return ", ".join(items)
    else:
        return "".join(items)

oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"])
