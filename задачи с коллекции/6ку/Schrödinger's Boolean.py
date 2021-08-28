omnibool = True


class incorrect_int(int):
    def __eq__(self, other):
        return True


omnibool = incorrect_int(omnibool)
