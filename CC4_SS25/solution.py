def sort_inventory(inventory, priority):
    """
    Sorts an inventory list in-place based on a given priority order.

    This function rearranges the items in `inventory` such that all items of type `priority[0]`
    appear first, followed by all items of type `priority[1]`, and finally all items of type `priority[2]`.
    The sorting should be done in O(N) time and O(1) space.

    Parameters:
    ----------
    inventory : List[int]
        A list of item IDs representing inventory. Each item in `inventory` is guaranteed
        to be one of the three types specified in `priority`.

    priority : List[int]
        A list of exactly three distinct integers that specify the desired order
        of sorting. The items in `inventory` should be rearranged to match this order.

    Returns:
    -------
    List[int]
        The modified `inventory` list, sorted in-place according to the `priority` order.

    Example:
    -------
    #>>> inventory = [2, 0, 0, 3, 3, 0, 2, 2]
    #>>> priority = [0, 2, 3]
    #>>> sort_inventory(inventory, priority)
    [0, 0, 0, 2, 2, 2, 3, 3]
    """
    counts = [0,0,0]
    for i in range(len(inventory)):  # count occurrences of nums
        if inventory[i] == priority[0]:
            counts[0] += 1
        elif inventory[i] == priority[1]:
            counts[1] += 1
        else:
            counts[2] += 1
    for i in range(len(inventory)):  # in-place sort based on priority and counts
        if counts[0] != 0:
            inventory[i] = priority[0]
            counts[0] -= 1
        elif counts[1] != 0:
            inventory[i] = priority[1]
            counts[1] -= 1
        else:
            inventory[i] = priority[2]
            counts[2] -= 1
    return inventory
