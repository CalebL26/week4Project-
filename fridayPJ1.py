# Instructions for the user
print("Welcome to the Mad Libs game!")
print("Please provide the following words when prompted:")

# Acquiring words from the player
large_object = input("Enter a large object: ")
large_objects_plural = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
first_food = input("Enter a food: ")
second_food = input("Enter another food: ")
large_object_singular = input("Enter another large object: ")

# Story with user inputs
mad_lib_story = f"I’ve had a very {adjective} day.\n" \
                f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n" \
                f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n" \
                f"But the waiter brought me {second_food}, which I was not hungry for.\n" \
                f"Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof."

# Printing the completed mad lib story
print("\nHere's your mad lib story:\n")
print(mad_lib_story)
