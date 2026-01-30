from exercise1.math_ops import square, cube
from exercise3.string_ops import count_vowels, reverse_string
from exercise4.text_analysis import analyze_text
import exercise1.math_ops as m
from exercise7.modules.calculator.operations import add, subtract
# from exercise7.modules.calculator import add, subtract [NOTE: BOTH WORKS]


print("Exercise 1")
print(square(4))
print(cube(3))


print("\n\nExercise 2")
print(count_vowels("ftujvynetmitpoibqwrbnmvli"))
print(reverse_string("bunny"))


print("\n\nExercise 3")
print(count_vowels("ftujvynetmitpoibqwrbnmvli"))
print(reverse_string("bunny"))


print("\n\nExercise 4")
print(analyze_text("ftujvynetmitpoibqwrbnmvli"))


print("\n\nExercise 5")
print(m.square(4))
print(m.cube(3))


print("\n\nExercise 5")
print(add(3, 5))
print(subtract(7, 3))
