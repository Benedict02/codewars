def period_is_late(last,today,cycle_length):
    if last.strftime("%Y") == today.strftime("%Y"):
        if abs(int(last.strftime("%j")) - int(today.strftime("%j"))) > cycle_length:
            return True
        else:
            return False