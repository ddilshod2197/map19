sonlar = [1, 2, 3, 4, 5, 6]

natija = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", sonlar))
print(natija)
# Natija: ['Toq', 'Juft', 'Toq', 'Juft', 'Toq', 'Juft']
