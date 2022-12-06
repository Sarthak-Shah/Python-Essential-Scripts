"""
Conway's Game of Life

critter : A critter is an animal. If you hear scratching noises in your ceiling at night, you can be sure that some kind
of critter is living in your attic.

attic : a space or room just below the roof of a building.

Biosphere : It's a relatively thin layer of the Earth's surface that supports life, reaching from a few kilometers into
the atmosphere to deep-sea vents. The biosphere is a global ecosystem made up of living organisms (biota) and the
 nonliving (abiotic) factors that provide them with energy and nutrients.

Conway's Game of Life is a game invented by mathematician John Conway in 1970. The rules are as follows:

Each cell lives in a square in a rectangular grid. A cell can either be dead or alive (alive cells are coloured blue in
 our demo). Before you start the game, you need to provide an initial state.
The game is now ready to begin, and this involves advancing through time one step at a time. A cell's fate depends on
the state of its 8 closest neighbours (our grid utilises wrapping, meaning a cell on the far left is thought of as a
neighbour of a cell on the far right, and the same principle applies at the top and bottom).

If a cell is alive, and 2 or 3 of it's neighbours are also alive, the cell remains alive.
If a cell is alive and it has more than 3 alive neighbours, it dies of overcrowding.
If a cell is alive and it has fewer than 2 alive neighbours, it dies of loneliness.
If a cell is dead and it has exactly 3 neighbours it becomes alive again.
Those 4 seemingly simple rules can result in wildy differing sequences.
Sometimes an initial state will create an unpredictable, chaotic sequence. Other times, it will create a repeating
sequence (such as the glider, pulsar, and spaceship from the preset dropdown). And other times, all cells will quickly
die off or stabilise into a static formation, known as a still life, such as a 2x2 square.

http://pi.math.cornell.edu/~lipa/mec/lesson6.html

The “game” is a zero-player game, meaning that its evolution is determined by its initial state,
requiring no further input. One interacts with the Game of Life by creating an initial configuration and
observing how it evolves, or, for advanced “players”, by creating patterns with particular properties.
"""
# sample input
"""
If we break down the grid, we can see that there are rows and columns. If we convert this to Python you can place lists 
within lists to mimic this behaviour.
"""

"""
Required flow:
1) get the initial starting pattern from the 6 hard-coded choices or from file
2) run a turn in the simulation
do while (user has not quit)
3) display the state of the world (before and after applying the rules for that turn)
    run a turn in the simulation
4) prompt the user (quit or continue to the next turn: the option to toggle debugging won't be displayed but the 
program will react to this selection)
5) copy the new world biosphere into the old world biosphere (write the code yourself, don't use a pre-created 
python function/method)
end loop
"""
# rows, cols = (10, 10)
# grid = [[" "]*cols]*rows


def sixthComplexCases():
    predefinedList = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", "*", " ", " ", " ", " "],
                        [" ", " ", " ", "*", "*", "*", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    return predefinedList

"""
File input option 2 (variable sized pattern for a list of any size): Reading the starting information from 
any arbitrarily sized rectangular file into a variable size 2D list (worth a greater number of marks) 
[One example input file]
The starting pattern of critters will be from any sized rectangular sized grid (minimum of 1 row or column 
to a maximum of 20 rows x 30 columns. 
"""


def readFileInput():
    """
    If there is any problems associated with the file (cannot open, file is empty, or there is an error during the
    actual read process) then the program will display an appropriate error message and repeatedly prompt the user for
    the name of the input file and begin the file read process anew.
    :param filepath: Input file name containing data
    :return: 2D list
    """
    while True:
        gatheredData = []
        flag = True
        while flag:
            try:
                filename = input("Enter filename with correct path ! ")
                final_filepath = filename + ".txt"
                fd = open(final_filepath, 'r')
            except FileNotFoundError:
                print("FileNotFoundError: Sir file not found ! please enter valid file name !")
            except OSError:
                print("OSError: Sir file seems not valid ! please enter valid file name !")
            else:
                gatheredData = fd.read().splitlines()
                if len(gatheredData) < 1:
                    print("EmptyFileError: it seems empty file ! Please input file"
                          " with atleast 10x10 2D array")
                    fd.close()
                else:
                    flag = False
        return gatheredData


# Function to get next generation from previous generaiton
def GetNextGeneration(grid, M, N):
    """

    :param grid:
    :param M: number of rows
    :param N: number of cols
    :return: pair of old and new biosperes
    """
    future = [[" " for i in range(M)] for j in range(N)]

    # Loop through every cell
    for l in range(M):
        for m in range(N):

            # finding no Of Neighbours that are alive
            aliveNeighbours = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= l + i < M and 0 <= m + j < N:
                        aliveNeighbours.append(grid[l + i][m + j])

            # The cell needs to be subtracted from
            # its neighbours as it was counted before
            aliveNeighbours.remove(grid[l][m])

            # Implementing the Rules of Life
            # Cell is lonely and dies
            if grid[l][m] == "*" and aliveNeighbours.count("*") < 2:
                future[l][m] = " "

            # Cell dies due to over population
            elif grid[l][m] == "*" and aliveNeighbours.count("*") > 3:
                future[l][m] = " "

            # A new cell is born
            elif grid[l][m] == " " and aliveNeighbours.count("*") == 3:
                future[l][m] = "*"

            # Remains the same
            else:
                future[l][m] = grid[l][m]
    return grid, future


def printBeforeAfterBiosperes(before:list, after:list, nrow=10, ncol=10):
    print("BEFORE", "AFTER", sep=" " * 15)
    for i in range(nrow):
        for j in range(ncol):
            print(before[i][j], end="|")
        print("-#   ", end=" ")
        for j in range(ncol):
            print(after[i][j], end="|")
        print()


def main():
    user_action = ''
    turn = 0
    initialStartingPattern = sixthComplexCases()
    # initialStartingPattern = readFileInput()
    while user_action != 'q':
        user_action = input("Hit enter to continue ('q' to quit):  ")
        if user_action == '':
            print("Turn #", turn)
            before, after = GetNextGeneration(initialStartingPattern, 10, 10)
            printBeforeAfterBiosperes(before, after)
            initialStartingPattern = after
            turn += turn


if __name__ == "__main__":
    main()
