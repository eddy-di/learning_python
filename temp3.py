def josephus(n, k):
    if n == 1:
        return 1  # The last person standing is the only person (position 1).

    # Initialize a list of people with positions 1 to n.
    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        # Find the next person to be eliminated.
        index = (index + k - 1) % len(people)
        eliminated_person = people.pop(index)

    return people[0]  # Return the position of the last person standing.

# Example usage:
n = 7  # Total number of people
k = 3  # Count after which a person is eliminated
survivor_position = josephus(n, k)
print(f"{survivor_position}")
