from operator import truediv


class CC0:
    def pairwise_sum(self, data, target_sum):
        # initialize dict to keep track of numbers encountered
        nums = {}

        # iterate over each number in data list
        for num in data:
            # calculate the number needed with 'num' to achieve 'target_sum'
            potential_pair = target_sum - num

            # check if potential pair number already exists in nums dict
            if potential_pair in nums:
                # looking up a val in dict is not iterative, O(1)
                return [potential_pair, num]
            else:
                # otherwise, mark current number as encountered by adding it to nums dict
                nums[num] = True

        # if no pair exists in the whole list, return an empty list
        return []

    def pairwise_sum_quadratic(self, data, target_sum):
        pass
