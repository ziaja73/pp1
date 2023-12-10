

def f(card_number):
    masked_number = card_number[:2] + '*' * (len(card_number)) + card_number[-4:]
    return masked_number

# Testujemy funkcję
print(f("5290312400019022"))  # Powinno zwrócić "52**********9022"