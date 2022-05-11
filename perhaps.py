class x:
    """
    This class allows function pipelining (see the example below).
    Functions are evaluated ltr bash style (hence the syntax).

    Constructing with a value i.e. x(10) means that the callable 
    returned by the pipeline takes no arguments:
        
        >>> f = x(10) | lambda y: y - 1 | str
        >>> f()
        '9'

    It can be evaluated by terminating it with an ellipsis:
        
        >>> f1 = lambda y: (y+98, y+101, y+98)
        >>> f2 = lambda y: [chr(el) for el in y]
        >>> x(10) | f1 | f2 | "".join | ...
        'lol'

    Constructing with x(...) means evaluation is deferred, and returns a 
    function of one parameter:

        >>> f = x(...) | lambda y: y - 1 | str
        >>> f(43)
        '42'

    Similar to the non-deferred case above, these expressions can be 
    evaluated inline by terminating the pipeline with the parameter:

        >>> f1 = lambda y: (y+98, y+101, y+98)
        >>> f2 = lambda y: [chr(el) for el in y]
        >>> x(...) | f1 | f2 | "".join | 10
        'lol'

    """
    def __init__(self, value=...):
        self.value = value
        self.call = lambda y: y

    def __or__(self, other):
        if other is ...:
            return self.value
        elif self.value is ...:
            oldcall = self.call
            self.call = lambda y: other(oldcall(y))
            return self
        elif self.value is not None:
            return x(other(self.value))
        
        return self
    
    def __call__(self, y, *_, **__):
        return self.call(self.value if self.value is not ... else y)

