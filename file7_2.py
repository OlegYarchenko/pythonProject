def correct_sentence(text):
    first_letter = text[0]
    my_text = text[1:]
    if my_text.endswith(".") is False:
        my_text += "."
    result = first_letter.capitalize() + my_text
    return result


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
