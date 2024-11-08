calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [spisok.lower() for spisok in list_to_search]

print(string_info('Lopuh'))
print(string_info('Repey'))
print(string_info('Metallolom'))
print(is_contains('Roza', ['tulpan', 'BANan', 'RoZa']))
print(is_contains('Val', ['Valentin', 'Karnaval']))
print(calls)