### Necessary imports
import os
import random
import requests

### Helpers
def _keyin_int(rank=None, default=None, description=None, should_be_positive=False):
    is_done = False
    while not is_done:
        if description is not None:
            if rank is not None:
                question_str = f'Please enter {description} {rank}'
            else:
                question_str = f'Please enter {description}'
        else:
            if rank is not None:
                question_str = f'Please enter integer value {rank}'
            else:
                question_str = f'Please enter an integer value'
                
        if default is not None:
            question_str += f' (Press Enter for default value {default}): '
        else:
            question_str += f': '
            
        number_str = input(question_str)
        if number_str == '':
            number = default
            is_done = True
        else:
            try:
                number = int(number_str)
                is_done = True
            except ValueError:
                print(f'"{number_str}" is not an integer value! Try again!')
                print()
            if is_done:
                if should_be_positive:
                    if number < 0:
                        print(f'{number} is not positive! Try again!')
                        print()
                        is_done = False
    return number


def _keyin_ints(rank=None, default=None, description=None, should_be_positive=False):
    is_done = False
    while not is_done:
        if description is not None:
            if rank is not None:
                question_str = f'Please enter a series of {description} {rank}, separated by spaces'
            else:
                question_str = f'Please enter a series of {description}, separated by spaces'
        else:
            if rank is not None:
                question_str = f'Please enter a series of integer numbers, separated by spaces {rank}'
            else:
                question_str = f'Please enter a series of integer numbers, separated by spaces'
                
        if default is not None:
            question_str += f' (Press Enter for default values {default}): '
        else:
            question_str += f': '
            
        numbers_str = input(question_str)
        if numbers_str == '':
            if default is None:
                numbers = []
            else:
                numbers = [int(x) for x in default.strip().split()]
            is_done = True
        else:
            try:
                numbers = [int(x) for x in numbers_str.strip().split()]
                is_done = True
            except ValueError:
                print(f'"{numbers_str}" should only contain integer values! Try again!')
                print()
            if is_done:
                if should_be_positive:
                    for number in numbers:
                        if number < 0:
                            print(f'{number} is not positive! Try again!')
                            print()
                            is_done = False
    return numbers


def _keyin_intmat(rank=None, default=None, description=None, should_be_positive=False):
    if default is None:
        default = [[1, 2], [3, 4]]
    first_row = _keyin_ints(rank=rank, default=' '.join([str(x) for x in default[0]]), description=description, should_be_positive=should_be_positive)
    if first_row == default[0]:
        print(f"\nWorking with default matrix: {default}")
        return default
    matrix = [first_row]
    count = 2
    while True:
        next_row = _keyin_ints(rank=None, default=None, description=f'{len(first_row)} integers for row {count}', should_be_positive=should_be_positive)
        if len(next_row) == 0:
            break
        elif len(next_row) != len(first_row):
            print(f'The row should contain {len(first_row)} elements, yours contains {len(next_row)}! Ignored...')
        else:
            count += 1
            matrix.append(next_row)
    print(f"\nWorking with matrix: {matrix}")
    return matrix
            

def _keyin_num(rank=None, default=None, description=None, should_be_positive=False):
    is_done = False
    while not is_done:
        if description is not None:
            if rank is not None:
                question_str = f'Please enter {description} {rank}'
            else:
                question_str = f'Please enter {description}'
        else:
            if rank is not None:
                question_str = f'Please enter value {rank}'
            else:
                question_str = f'Please enter a value'
                
        if default is not None:
            question_str += f' (Press Enter for default value {default}): '
        else:
            question_str += f': '
            
        number_str = input(question_str)
        if number_str == '':
            number = default
            is_done = True
        else:
            try:
                number = float(number_str)
                is_done = True
            except ValueError:
                print(f'"{number_str}" is not a value! Try again!')
                print()
            if is_done:
                if should_be_positive:
                    if number < 0:
                        print(f'{number} is not positive! Try again!')
                        print()
                        is_done = False
                    
    return number


def _keyin_nums(rank=None, default=None, description=None, should_be_positive=False):
    is_done = False
    while not is_done:
        if description is not None:
            if rank is not None:
                question_str = f'Please enter a series of {description} {rank}, separated by spaces'
            else:
                question_str = f'Please enter a series of {description}, separated by spaces'
        else:
            if rank is not None:
                question_str = f'Please enter a series of numbers, separated by spaces {rank}'
            else:
                question_str = f'Please enter a series of numbers, separated by spaces'
                
        if default is not None:
            question_str += f' (Press Enter for default values {default}): '
        else:
            question_str += f': '
            
        numbers_str = input(question_str)
        if numbers_str == '':
            numbers = [float(x) for x in default.strip().split()]
            is_done = True
        else:
            try:
                numbers = [float(x) for x in numbers_str.strip().split()]
                is_done = True
            except ValueError:
                print(f'"{numbers_str}" should only contain numbers! Try again!')
                print()
            if is_done:
                if should_be_positive:
                    for number in numbers:
                        if number < 0:
                            print(f'{number} is not positive! Try again!')
                            print()
                            is_done = False
    return numbers


def _keyin_str(rank=None, default=None, description=None):
    if description is not None:
        if rank is not None:
            question_str = f'Please enter {description} {rank}'
        else:
            question_str = f'Please enter {description}'
    else:
        if rank is not None:
            question_str = f'Please enter string {rank}'
        else:
            question_str = f'Please enter a string'
    if default is not None:
        question_str += f' (Press Enter for default "{default}"): '
    else:
        question_str += f': '
        
    input_str = input(question_str)
    if input_str == '':
        string = default
    else:
        string = input_str
    return string

### Functions specific to the set of challenges presented here
def test_challenge_1(f):
    a = _keyin_int(default=3, description="an integer value for a")
    b = _keyin_int(default=7, description="an integer value for b")
    c = _keyin_int(default=5, description="an integer value for c")
    result = f(a, b, c)
    if result is None:
        print("Your function does not return anything (yet)!")
    elif type(result) != int:
        print(f"Your function does not return an integer, but an object of type {type(result)}")
    else:
        print(f"\nYour function {f.__name__} determines that {result} is the largest value of {a}, {b} and {c}.")


def test_challenge_2a(f):
    # From exam 2021-03-15
    while True:
        square = input('Enter a board square, A1 ... H8: ').strip()
        if len(square) != 2:
            print('Enter a two character string A1 ... H8!')
            continue
        if square[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print('The first character should be a A .. H!')
            continue
        if not square[1].isdigit():
            print('The second character should be an integer in range 1 .. 8!')
            continue
        try:
            if int(square[1]) < 1 or int(square[1]) > 8:
                print('The second character should be an integer in range 1 .. 8!')
                continue
            break
        except ValueError:
            print('The second character should be an integer in range 1 .. 8!')
            continue
    
    print()
    result = f(square.upper())
    if result is None:
        print("Your function does not return anything (yet)!")
    elif type(result) != list:
        print(f"Your function does not return a list, but an object of type {type(result)}")
    else:
        print(f'A rook on square {square} can move to: ', result)
    

def test_challenge_2b(f):
    # From exam 2021-03-15
    raw_data = [1.0, 2.0, 'Missing', 4.0, 5.0, 'Missing', 'Missing', 8.0, 'Missing', 10.0]

    print('The default input is:', raw_data)
    print('Press Enter to use that, or enter any combination of floats where capital M indicates a missing value: ')
    print("Example: 1.0 2.0 M 4.0 for [1.0, 2.0, 'Missing', 4.0]")
    print()

    while True:
        string = input('Enter for default, or string with missing values: ')
        if string != '':
            raw_list = string.strip().split()
            raw_data = []
            correct = True
            for ch in raw_list:
                if ch == 'M' or ch == 'Missing':
                    raw_data.append('Missing')
                elif str(ch).isnumeric():
                    raw_data.append(float(ch))
                else:
                    print(f"Oops! '{ch}' is neither 'M', nor a numeric value!")
                    correct = False
            if correct:
                break
        else:
            break
        
    print()
    result = f(raw_data)
    if result is None:
        print("Your function does not return anything (yet)!")
    elif type(result) != float:
        print(f"Your function does not return a float value, but an object of type {type(result)}")
    else:
        print('The raw_data', raw_data, 'has an average of', result)


def _keyin_board(rank=None, default=[[1, 0, 0], [1, 0, 0], [0, 1, 0]], description='board', should_be_positive=False):
    defaults = []
    for row in default:
         defaults.append(' '.join([str(x) for x in row]))

    rows, cols = 3, 3
    matrix = []
    print()
    
    for row in range(rows):
        row_values = []
        while len(row_values) != cols:
            default = defaults[row]
            not_ok = True
            while not_ok:
                row_values = _keyin_ints(rank=row+1, default=default, description=f'{cols} zeroes and ones for row', should_be_positive=should_be_positive)
                for v in row_values:
                    if v < 0 or v > 1:
                        print("Numbers should be either zero or one!\n\n")
                        break
                else:
                    not_ok = False
            if len(row_values) != cols:
                print()
                print(f'Please enter {cols} zeroes and ones!')
            else:
                break
        matrix.append(row_values)    
    return matrix


def test_challenge_3a(f):
    board = _keyin_board()
    result = f(board)
    print()
    if result == 0:
        print("Your function returns '0' and hence indicates that the center cell will be dead.")
    elif result == 1:
        print("Your function returns '1' and hence indicates that the center cell will be alive.")
    else:
        print("Your function returns neither '0', nor '1'. Are you sure your function is ready to be tested?")
        
        
def test_challenge_3b(f):
    timings = []
    timings.append(_keyin_int(rank=None, default=49, description='timing Rotterdam-Utrecht (A20-A12, part 0)', should_be_positive=True))
    timings.append(_keyin_int(rank=None, default=28, description='timing Utrecht-Hoevelaken (A27-A1, part 1)', should_be_positive=True))
    timings.append(_keyin_int(rank=None, default=21, description='timing Utrecht-Hoevelaken (A28, part 2)', should_be_positive=True))
    timings.append(_keyin_int(rank=None, default=51, description='timing Utrecht-Apeldoorn (A12-A50, part 3)', should_be_positive=True))
    timings.append(_keyin_int(rank=None, default=32, description='timing Hoevelaken Apeldoorn (A1, part 4)', should_be_positive=True))
    result = f(timings)
    print()
    if type(result) == int:
        print(f"The shortest route from Rotterdam to Apeldoorn takes {result} minutes.")
    else:
        print(f"Your function does not return an integer value. Is it working correctly?")
        
        
def test_challenge_3c(f):
    default = ['The Great Gatsby', 'Pride and Prejudice', 'The Catcher in the Rye', 'Wuthering Heights', 'Frankenstein']
    book = input("Enter first book title for John (Enter for default example list of books)")
    if book == "":
        john = default
    else:
        john = [book]
        count = 1
        while book is not None:
            count += 1
            book = _keyin_str(rank=count, default=None, description='book title for John (leave empty if done)')
            if book is not None:
                john.append(book)
    default = ['Wuthering Heights', 'The Adventures of Huckleberry Finn', 'Jane Eyre', 'Pride and Prejudice', 'Animal Farm']
    book = input("Enter first book title for Mary (Enter for default example list of books)")
    if book == "":
        mary = default
    else:
        mary = [book]
        count = 1
        while book is not None:
            count += 1
            book = _keyin_str(rank=count, default=None, description='book title for Mary (leave empty if done)')
            if book is not None:
                mary.append(book)
    result = f(john, mary)
    if result is None:
        print("\nYour function does not (yet) return a value!")
    elif type(result) != list:
        print(f"\nYour function does not return a list, but an object of type {type(result)}!")
    else:
        print("Books read by John:\n *", "\n * ".join(john), "\n")
        print("Books read by Mary:\n *", "\n * ".join(mary), "\n")
        print("Books read only by John or Mary:\n *", "\n * ".join(result), "\n")
        
        
### Download assertions.pickle (prevent overwriting)
if not os.path.exists('assertions.pickle'):
    assertion_obj = requests.get("https://raw.githubusercontent.com/jjengelberts/precourse-test/main/assertions.pickle")
    if assertion_obj.status_code != 200:
        print('Could not download assertions.pickle, hence tests can not be automatically verified!')
    else:
        try:
            with open('assertions.pickle', 'wb') as f:
                f.write(assertion_obj.content)
            print('Test cells imported OK')
        except:
            print('Assertions could not be written to disk!')
