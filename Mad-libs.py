# mad-libs
# string concatenation (a.k.a. how to put strings together)

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
verb1 = input("Verb: ")
color = input("color: ")
name = input("name: ")

madlib = f'Once upon a time, there was a town very {adj1}... It was {adj2} and strangers used to come here because they' \
         f' they loved to {verb1}. Women there were {adj3} and they were usually all dressed in {color}' \
         f' but one day a man called {name} arrived and his presence changed a lot of things.'

print(madlib)
