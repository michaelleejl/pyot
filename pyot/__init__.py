from metamodel import get_metamodel
from textx import language


@language("pyot", "*.pyot")
def pyot():
    """A language for controlling IOT devices"""
    return get_metamodel()
