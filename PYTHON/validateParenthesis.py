"""
Dada una cadena que contiene solo los caracteres (, ), {, }, [ y ], determina si la cadena es válida (es decir, si los paréntesis están correctamente cerrados).

Ejemplo:

Input: "()[]{}"

Output: True
"""

def validateParenthesis(txt):
    _mapping = {'(': ')', '{': '}', '[': ']'}

    _stack = []

    for i in txt:
        if i in _mapping.keys():
            _stack.append(i)
        elif i in _mapping.values():
            if _stack and i == _mapping[_stack[-1]]:
                _stack.pop()
            
    return not _stack 


txt = "()[]{}"
print(validateParenthesis(txt))
