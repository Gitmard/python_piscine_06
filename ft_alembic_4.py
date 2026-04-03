#!/usr/bin/python3

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print(f"Testing create_air: Air {alchemy.create_air()}")

    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    print("Testing the hidden create_earth: ", end="")
    alchemy.create_earth()
