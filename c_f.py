import pyperclip


def process_input(number, name):
    """Generate the filename and put it into the clipboard."""

    name = name.replace(' ', '_')
    result = f"q{number}_{name}"
    print(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    inputs = input("Please enter a kyu and a name, separated by a space: ").split()
    number = inputs[0]
    name = ' '.join(inputs[1:])
    process_input(number, name)
