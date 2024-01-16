

def badge_maker(name):
    """Creates and returns a badge message."""
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    """Creates and returns a list of badge messages for a list of names."""
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    """Assigns each speaker to a room and returns a list of room assignment messages."""
    return [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(names, 1)]


def printer(names):
    """Prints the badge messages and room assignment messages for a list of names."""
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
