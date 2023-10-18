import string

#  a...z
#  aa ab ac ad ...  zw zy zx zz
#  aaa aab aac... zzw zzx zzy zzz
#  aaaa .... zzzz

LETTERS = string.ascii_lowercase

class AlphaIncrement:
    def __init__(self, *args):
        if len(args) == 1:
            self._stop_value = args[0]
            self._level = 1
            self._ord = ord('a')
        elif len(args) == 2:
            start, stop = args
            self._ord = ord(start[0])
            self._level = len(start)
            self._stop_value = stop
        else:
            raise ValueError(f"AlphaIncrement takes one or two arguments, not {len(args)}")
        self._value = self._level * chr(self._ord)

    def __iter__(self):
        return self
    
    def __next__(self):
        self._calculate_next()
        if self._value == self._stop_value:
            raise StopIteration
        return self._value
    
    def _calculate_next(self):
        end_of_level = 'z' * self._level 
        if self._value == end_of_level:
            self._level += 1
            self._ord = ord('a')
        self._value = self._level * chr(self._ord)
        self._ord += 1
        
if __name__ == "__main__":
    ci1 = AlphaIncrement('ddd')
    for x in ci1:
        print(x, end=' ')
    print("\n")

    ci2 = AlphaIncrement('aa', 'rr')
    print(' '.join(ci2), '\n')

    ci3 = AlphaIncrement('f', 'x')
    print(' '.join(ci3), '\n')

    # ci4 = AlphaIncrement('a', 'z', 'vv')  INVALID
