from contextlib import contextmanager

@contextmanager
def safe_file_edit(filename):
    try:
        with open(filename, 'r+') as file:
            initial_state = file.read()
            edited_state = initial_state

            yield edited_state

            if edited_state != initial_state:
                file.seek(0)  # Move the file pointer to the beginning
                file.truncate()  # Clear the file
                file.write(edited_state)  # Write the edited content
    except Exception as e:
        print(f"Error: {e}")
# Usage as a context manager
# with safe_file_edit('example.txt', 'r+') as file_content:
    # Make changes to the file content
    # file_content += "This is an additional line.\n"
    # file_content += "Another line."

    # Simulate an error
    # raise ValueError("Simulated error")

# The file is restored to its initial state upon error


print('TEST_1:')
with safe_file_edit('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')
    
with open('undertale.txt') as file:
    print(file.read())

print('TEST_2:')
with safe_file_edit('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
    
with safe_file_edit('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())
