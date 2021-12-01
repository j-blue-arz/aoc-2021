def read_input():
    with open("input") as file:
        return file.read().strip()

def iterate_examples(example_strings):
    examples = list(map(str.strip, example_strings))
    while examples and not examples[-1]: examples.pop()
    return examples

def run_with_examples_and_input(examples, solver, title, with_input=True):
    input = read_input()
    print(title)
    for num, example in enumerate(iterate_examples(examples)):
        result = solver(example)
        if result is not None:
            print(f"Result example {num}:\n{result}")
            print("-"*10)
    if with_input:
        result = solver(input)
        if result is not None:
            print("-"*15)
            print(f"Result real:\n{result}")
        print("="*15)