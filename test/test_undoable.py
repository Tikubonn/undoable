
import pytest
from undoable import Undoable

def test_undo ():

  #初期値から変更されていなければ .undo は実行できない。

  ud = Undoable(1) #(1)
  assert ud.can_undo == False
  with pytest.raises(ValueError):
    ud.undo()

  #初期値から変更されていれば .undo が実行できる。

  ud.set(2) #(1 2)
  assert ud.get() == 2
  assert ud.can_undo == True

  #変更された値が残っていなければ .undo は実行できない。

  ud.undo() #(1)
  assert ud.get() == 1
  assert ud.can_undo == False
  with pytest.raises(ValueError):
    ud.undo()

def test_redo ():

  #.undo が実行されていなければ .redo は実行できない。

  ud = Undoable(1)
  ud.set(2)
  ud.get() == 2
  ud.can_undo == True
  ud.can_redo == False
  with pytest.raises(ValueError):
    ud.redo()

  #.undo が実行されていれば .redo が実行できる。

  ud.undo() #(1) . (2)
  ud.get() == 1
  ud.can_undo == False
  ud.can_redo == True

  #.undo された値が残っていなければ .redo は実行できない。

  ud.redo() #(1 2)
  ud.get() == 2
  ud.can_undo == True
  ud.can_redo == False

def test_fix ():

  #.fix が実行されるといままでの変更履歴が削除されます。

  ud = Undoable(1) #(1)
  assert ud.get() == 1
  assert ud.can_undo == False
  assert ud.can_redo == False

  ud.fix() #(1)
  assert ud.get() == 1
  assert ud.can_undo == False
  assert ud.can_redo == False

def test_fix2 ():

  #.fix が実行されるといままでの変更履歴が削除されます。

  ud = Undoable(1) #(1)
  ud.set(2) #(1 2)
  assert ud.get() == 2
  assert ud.can_undo == True
  assert ud.can_redo == False

  ud.fix() #(2)
  assert ud.get() == 2
  assert ud.can_undo == False
  assert ud.can_redo == False

def test_fix3 ():

  #.fix が実行されるといままでの変更履歴が削除されます。

  ud = Undoable(1) #(1)
  ud.set(2) #(1 2)
  assert ud.get() == 2
  assert ud.can_undo == True
  assert ud.can_redo == False

  ud.undo() #(1) . (2)
  assert ud.get() == 1
  assert ud.can_undo == False
  assert ud.can_redo == True

  ud.fix() #(1)
  assert ud.get() == 1
  assert ud.can_undo == False
  assert ud.can_redo == False
