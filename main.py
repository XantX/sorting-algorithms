import random
import time
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import quick_sort
from heapsort import heap_sort

ARRAY_SIZE = 1000000

def track_time(function, array):
    inicio = time.time()
    function(array)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(function.__name__.upper(),"execution time:", tiempo_ejecucion, "seconds")

def track_divide_time(function, array):
    inicio = time.time()
    function(array, 0, len(array) - 1)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(function.__name__.upper(),"execution time:", tiempo_ejecucion, "seconds")

if __name__ == "__main__":
    my_array = list(range(1, ARRAY_SIZE))
    random.shuffle(my_array)

    print("Ordering size arrangements:", ARRAY_SIZE)

    #track_time(bubble_sort, my_array)
    #track_time(insertion_sort, my_array)
    arrMr = my_array.copy()
    track_divide_time(merge_sort, arrMr)
    arrQk = my_array.copy()
    track_divide_time(quick_sort, arrQk)
    track_time(heap_sort, my_array)
