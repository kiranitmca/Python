
# def learner(name):
#     print(f"{name} is learning Python.")

# learner("Alice")


# def pet(name,animal_type):
#     print(f"{name} is a {animal_type}.")
# pet("Buddy", "dog")

# Variable length arguments

def sum_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

sum1 = sum_numbers(1, 2, 3)
sum2 = sum_numbers(4, 5)
print(f"Sum 1: {sum1}")
print(f"Sum 2: {sum2}")