from typing import List, Union

def bubble_sort(arr : List , simulation : bool = False) -> List:
    """Sorts A List using bubble sort algorithm
    https://en.wikipedia.org/wiki/Bubble_sort
    Worst-case performance: O(N^2)

    Parameters:
        arr(List) : Unsorted List 
        simulation(bool) : to enable simulation (default argument is False) 

    Returns:
        arr(List) : Returns sorted List

    """

    def swap(i : int, j : int) -> None:
        """Swaps two element of List 

        Parameters:
            i(int) : index of first element
            j(int) : index of second element

        Returns:
            None : Function returns nothing

        """
        arr[i], arr[j] = arr[j], arr[i]

    n : int = len(arr)
    swapped : bool = True
    
    iteration : int = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    x : int = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print("iteration",iteration,":",*arr)
                    
    return arr

def insertion_sort(arr : List , simulation : bool = False) -> List:
    """ Insertion Sort
    Complexity: O(n^2)
    1: Iterate from arr[1] to arr[n] over the array. 
    2: Compare the current element (key) to its predecessor. 
    3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
    """
    
    iteration : int = 0
    if simulation:
        print("iteration", iteration, ":", *arr)
        
    for i in range(len(arr)):
        cursor : Union[int, float, complex, str] = arr[i]
        pos : int = i
        """ Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position"""
        
        while pos > 0 and arr[pos - 1] > cursor:
            """ Swap the number down the list"""
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        """ Break and do the final swap"""
        arr[pos] = cursor
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)

    return arr