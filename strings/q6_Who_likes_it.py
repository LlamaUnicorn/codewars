# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# match case
# if-else

def likes(names):
    match names:
        case []:
            return 'no one likes this'
        case [name]:
            return f'{name} likes this'
        case [name1, name2]:
            return f'{name1} and {name2} like this'
        case [name1, name2, name3]:
            return f'{name1}, {name2} and {name3} like this'
        case [name1, name2, *args]:
            num_likes = len(names)-2
            return f'{name1}, {name2} and {num_likes} others like this'


print(likes(['Brian J. Mason', 'Nene Romanova', 'Galatea', 'Sylia Stingray', 'Largo', 'Anri', 'Priscilla S. Asagiri',
     'Macky Stingray', 'Nigel', 'Sylvie', 'Linna Yamazaki']))


# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
