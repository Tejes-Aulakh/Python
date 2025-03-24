def main():
    names = ["Trevor", "Fanklin", "Micheal", "Coby"]
    for name in names:
        print(write_letter(name, "Tejes-Aulakh"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Dear {receiver},
    
       You are cordially invited to a dinner at
       warly ct novi  this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """


main()