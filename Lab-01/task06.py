import time

def display_grid(grid):
    print("\nCurrent Environment Status:")
    print(f" {grid['a']}  {grid['b']}  {grid['c']} ")
    print(f" {grid['d']}  {grid['e']}  {grid['f']} ")
    print(f" {grid['g']}  {grid['h']}  {grid['j']} ")
    print("-------------------------")

def firefighting_robot():
    grid = {
        'a': ' ', 'b': ' ', 'c': '🔥',
        'd': ' ', 'e': '🔥', 'f': ' ',
        'g': ' ', 'h': ' ', 'j': '🔥'
    }
    
    path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    
    print("Robot starting at room 'a'.")
    display_grid(grid)
    
    for room in path:
        print(f"Robot entering room '{room}'...")
        
        if grid[room] == '🔥':
            print(f"Fire detected in room '{room}'! Extinguishing...")
            grid[room] = ' '
            print(f"Fire in room '{room}' has been extinguished.")
        
        display_grid(grid)
        time.sleep(1)
    
    print("All rooms have been checked. Final environment status:")
    display_grid(grid)
    print("All fires have been extinguished!")

firefighting_robot()
