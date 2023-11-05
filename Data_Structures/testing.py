from structure.linked_list import SLL


def test_add_first():
    sll = SLL()
    for i in range(10):
        sll.add_first(i)
    for i in range(10):
        assert sll[i] == i, "element %d not found" %i

# test_add_first()

sll = SLL()
sll.add_first(8)
sll.add_after(8, 9)
sll.add_last(10)
sll.show_all()
# sll.del_first()
# sll.del_last()
# sll.delete(8)
# sll.show_all()
try:
    for i in range(10):
        print(sll[i])
except Exception as err:
    print(f"Error {type(err)}:",err)
print("everything good")


def division(x,y):
  assert y!=0, "y cannot be zero"
  print(x/y)

try:
  division(10,0)
except AssertionError as msg:
  print(msg)