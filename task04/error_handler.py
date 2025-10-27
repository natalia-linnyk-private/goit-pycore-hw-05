def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as error:
            return error.args[0] if error.args else "Error accessing contacts"
        except ValueError as error:
            return error.args[0] if error.args else "Wrong format of input data"
        except IndexError as error:
            return error.args[0] if error.args else "Not enough count of arguments"
    return inner