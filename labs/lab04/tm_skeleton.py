import sys

BLANK = "λ"  
START_STATE = 0
MOVES = {"R": 1, "L": -1}

def read_program(filename):
    """ Read a program into a dictionary; returns (program, accept_states). """
    program = {}
    accept_states = set()
    with open(filename, encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if not parts or parts[0] == "c":
                continue  # blank line or comment
            if parts[0] == "accept":
                accept_states.update(int(s) for s in parts[1:])
                continue
            if len(parts) != 5:
                print("skipping malformed line:", line.rstrip())
                continue
            state, symbol, write, direction, new_state = parts
            key = (int(state), symbol)
            value = (write, MOVES[direction], int(new_state))
            program[key] = value
    return program, accept_states

def run(program:dict, accept_states:set, tape:list) -> None:
    state = START_STATE
    read = -1
    i = 0
    while not state in accept_states:
        
        if i >= len(tape):
            read = BLANK
        else:
            read = tape[i]
        
        write, move, new_state = program[(state, read)]

        if i >= len(tape):
            tape.append(write)
        else:
            tape[i] = write
        i += move
        state = new_state

        print(f'tape: {tape}')

    

def main():
    if len(sys.argv) != 3:
        print("usage: python3 tm.py <program file> <input tape>")
        print("example: python3 tm.py tm01.txt #0110")
        sys.exit(1)
    program, accept_states = read_program("./programs/" + sys.argv[1])
    tape = list(sys.argv[2])

    # for debugging:
    for key, val in program.items():
        print(f"{key} -> {val}")

    # you should write the function run():
    run(program, accept_states, tape)

main()