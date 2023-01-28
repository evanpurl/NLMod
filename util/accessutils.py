
async def whohasaccess():
    """

    :rtype: list
    """
    with open("util/access.txt") as access:  # Runs this as if it was in the main directory.
        data = access.read()
        datalist = data.split("\n")
    return datalist