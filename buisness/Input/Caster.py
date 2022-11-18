
def string_2_string(gui_input):
    if isinstance(gui_input, str):
        string_input = ''.join(_ for _ in gui_input if _.isalnum())
        if string_input.isalnum():
            return string_input
        return None
    return None
