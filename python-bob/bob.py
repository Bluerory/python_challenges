#
# Skeleton file for the Python "Bob" exercise.
#
# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.


def hey(what: str):
    what = what.strip()

    if not what or what.isspace():
        return 'Fine. Be that way!'

    if what.endswith('?'):
        if what.isupper():
            pass
        else:
            return 'Sure.'

    if what.isupper():
        return 'Whoa, chill out!'

    else:
        return 'Whatever.'
