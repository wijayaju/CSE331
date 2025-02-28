def non_constructible_change(coins):
    """
    Determines the smallest amount of money (change) that cannot be created
    using any combination of the given coin denominations.

    This function takes an array of positive integers representing coin
    denominations and computes the minimal value that cannot be constructed
    using any subset of the coins.

    The algorithm follows these steps:
    1. Sort the coins array.
    2. Iterate through the coins, keeping track of the maximum constructible
       change so far.
    3. Identify the first gap in constructible change.

    Parameters:
    ----------
    coins : list of int
        A list of positive integers, where each integer represents a coin
        denomination.

    Returns:
    -------
    int
        The smallest amount of money that cannot be constructed using the
        given coin denominations.

    Example:
    --------
    >>> non_constructible_change([1, 2, 5, 10])
    4

    Explanation:
    Given the coins [1, 2, 5, 10], the smallest amount of change that
    cannot be created is 4. This is determined by analyzing combinations
    of the coins and identifying gaps in constructible sums.
    """
    # check if list is empty
    if len(coins) == 0:
        return 1
    # check if list has just one coin
    elif len(coins) == 1:
        # check if coin is a penny
        if coins[0] == 1:
            return 2
        else:
            return 1
    else:
        # sort list
        for i in range(len(coins)):
            # find min
            min_index = i
            for j in range(i + 1, len(coins)):
                # check if change is less than current min val
                if coins[j] < coins[min_index]:
                    # set min
                    min_index = j
            # swap vals
            coins[i], coins[min_index] = coins[min_index], coins[i]
    # find non-constructible
    max_constructible = 0
    for change in coins:
        # check for first gap in constructible
        if change > max_constructible + 1:
            break
        # add the change to constructible
        max_constructible += change
    # otherwise, non-constructible is 1 more than sum
    max_constructible += 1
    return max_constructible
