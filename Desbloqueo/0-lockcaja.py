#!/usr/bin/python3

def desbloqueo(caja):

    Boxe = [0]

    for key in Boxe:
        for new_key in caja[key]:
            if new_key <= len(caja) - 1 and new_key not in Boxe:
                Boxe.append(new_key)

    if len(Boxe) == len(caja):
        return True
    else:
        return False
      
