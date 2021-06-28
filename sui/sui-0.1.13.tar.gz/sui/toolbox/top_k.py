"""Top k function for lists or tuples
Date: 26/Feb/2021
Author: Li Tang
"""
from typing import Union, List

__author__ = ['Li Tang']
__copyright__ = 'Li Tang'
__credits__ = ['Li Tang']
__license__ = 'MIT'
__version__ = '0.1.11'
__maintainer__ = ['Li Tang']
__email__ = 'litang1025@gmail.com'
__status__ = 'Production'


def top_k(data: Union[list, tuple], k: int, axis: int = 1, target: int = 0, target_only: bool = False,
          desc: bool = True) -> List[list or tuple]:
    """Function to return the top k values in the input list/tuple

    Args:
        data: input data to be sorted consists of lists or tuples
        k: the length of result to return
        axis: the dimension in the list/tuple in data for sorting
        target: the target dimension to return after sorting
        target_only: if target_only is True, the result contains only the target dimension in data;
        otherwise return all dimensions in data
        desc: True for descending and False for ascending

    Returns:
        a list sorted by target dimension with length no greater than k

    Examples:
        >>> data = (('Beijing', 8610, 'CN'), ('London', 4420, 'UK'), ('Zhuzhou', 86731, 'CN'), ('Manchester', 44121, 'UK'))
        >>> top_k(data=data, k=3, axis=1, target=0, target_only=False, desc=True)
        [('Zhuzhou', 86731, 'CN'), ('Manchester', 44121, 'UK'), ('Beijing', 8610, 'CN')]

    """

    def __push(item, data, axis, desc):
        for idx in range(len(data) - 1, -1, -1):
            if desc is True and data[idx][axis] >= item[axis] or desc is False and data[idx][axis] <= item[axis]:
                result = data[:idx + 1]
                result.append(item)
                result.extend(data[idx + 1:])
                return result
        data.insert(0, item)
        return data

    result = []

    for item in data:
        if len(result) < k or desc is True and item[axis] > result[-1][axis] or desc is False and item[axis] < \
                result[-1][axis]:
            result = __push(item, result, axis=axis, desc=desc)
        if len(result) > k:
            result = result[:k]

    return [i[target] for i in result] if target_only else result
