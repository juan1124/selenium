
__author__ = 'zk'


def test(name):
    #name='PeopleManager.PeopleManagerUnit.PeopleMnagerUnitC.Test_ImportPerson'
    module=None
    parts = name.split('.')
    if module is None:
        parts_copy = parts[:]

        while parts_copy:
            try:
                module = __import__('.'.join(parts_copy))
                break
            except ImportError:
                del parts_copy[-1]
                if not parts_copy:
                    raise
        parts = parts[1:]
    obj = module
    print(obj)
    for part in parts:
        parent, obj = obj, getattr(obj, part)
        print('obj:%s'% (obj))
        print('parent:%s'% (parent))


if __name__ == '__main__':
    test('PeopleManager.PeopleManagerUnit.PeopleMnagerUnitC.Test_ImportPerson')