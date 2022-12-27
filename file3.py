# A python program to implement tower of hanoi using recursion

"""
The Tower of Hanoi is a mathematical puzzle that consists of three rods and a 
number of disks of different sizes. The goal is to move all the disks from the
first rod to the third rod, following these rules:

* Only one disk can be moved at a time.
* Each move consists of taking the upper disk from one of the rods and placing it 
  on top of another rod, or on an empty rod.
* No disk may be placed on top of a smaller disk.
"""

#Define the tower of hanoi function
def tower_of_hanoi(n, source, destination, auxiliary):
    #If there is only one disk, move it from source to destination
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    #Move n - 1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    #Move the remaining disk from source to destination
    print("Move disk", n, "from source", source, "to destination", destination)

    #Move the n - 1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

#Define the main function
def main():
    #Define the number of disks
    n = 4

    #Call the tower of hanoi function
    tower_of_hanoi(n, 'A', 'C', 'B')

#Call the main function
if __name__ == '__main__':
    main()