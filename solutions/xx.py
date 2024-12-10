# TODO replace with AOC day
day: str = "00"

# TODO replace with test input and corresponding answers
test: str = """
"""
pt1_ans: int = 0
pt2_ans: int = 0


def parse_input(string: str):
    ...


def pt1():
    ...


def pt2():
    ...


def main(input: str):
    # TODO parse input and test

    assert pt1_ans == pt1(test)
    assert pt2_ans == pt2(test)


if __name__ == "__main__":
    with open(f'puzzles/{day}.txt', 'r') as f:
        input = f.read()
        main(input)
