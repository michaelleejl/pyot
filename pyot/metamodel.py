from textx import metamodel_from_file
from textx.scoping.providers import RelativeName, FQN


class Space(object):
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name')
        self.tags = kwargs.pop('tags')
        self.devices = kwargs.pop('devices')
        self.spaces = kwargs.pop('spaces')


def get_metamodel():
    # Step 1: Import the metamodel
    metamodel = metamodel_from_file("pyot.tx", classes=[Space])

    # Step 2: Register scope providers.
    # Scope providers are used to resolve references in the .tx file
    # This allows rules in the .tx file to refer to other rules
    # Two scope providers are registered - FQN (Fully Qualified Name) and RelativeName
    metamodel.register_scope_providers({
        '*.*': FQN(),
        'Testcase.config': RelativeName('scenario.configs')
    })

    return metamodel
