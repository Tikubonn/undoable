
from typing import Any

class Undoable:

  """アンドゥ・リドゥの機能を提供します。

  Examples
  --------
  >>> ud = Undoable(1)
  >>> ud.set(2)
  >>> ud.get()
  2
  >>> ud.undo()
  >>> ud.get()
  1
  >>> ud.redo()
  >>> ud.get()
  2
  """

  _values:list[Any]
  _undoable_count:int
  _redoable_values:list[Any]

  def __init__ (self, initial_value:Any):
    self._values = [initial_value]
    self._undoable_count = 0
    self._redoable_values = []

  def set (self, value:Any):

    """新たな値を設定します。

    設定された値は `.undo` メソッドにより元の値に復元されます。

    Parameters
    ----------
    value : Any
      新たに設定される値
    """

    self._values.append(value)
    self._undoable_count += 1
    self._redoable_values.clear()

  def get (self) -> Any:

    """現在設定されている値を返します。

    Returns
    -------
    Any
      現在設定されている値
    """

    if self._values:
      return self._values[-1]
    else:
      raise ValueError("Object has an illegal state: {:s}".format(repr(self)))

  def fix (self):

    """値の変更履歴を抹消します。

    このメソッドの実行後、新たな値が設定されるまで `.undo` メソッドによる値の復元は行えません。
    """

    if self._values:
      last = self._values[-1]
      self._values.clear()
      self._values.append(last)
      self._undoable_count = 0
      self._redoable_values.clear()
    else:
      raise ValueError("Object has an illegal state: {:s}".format(repr(self)))

  @property
  def can_undo (self) -> bool:

    """`.undo` メソッドを実行して、現在値を変更前の値に復元できるかを判定します。

    Returns
    -------
    bool
      アンドゥ可能ならば `True` そうでなければ `False` が返されます。
    """

    return 0 < self._undoable_count

  def undo (self):

    """過去の変更履歴を基に、現在値を過去の値に復元します。
    """

    if 0 < self._undoable_count:
      value = self._values.pop()
      self._undoable_count -= 1
      self._redoable_values.append(value)
    else:
      raise ValueError("Object has never modified: {:s}".format(repr(self)))

  @property
  def can_redo (self) -> bool:

    """`.redo` メソッドを実行して、復元された現在値を復元前に戻せるのかを判定します。

    Returns
    -------
    bool
      リドゥ可能ならば `True` そうでなければ `False` が返されます。
    """

    return bool(self._redoable_values)

  def redo (self):

    """`.undo` メソッドにより復元された現在値を、復元前の値に戻します。
    """

    if self._redoable_values:
      value = self._redoable_values.pop()
      self._values.append(value)
      self._undoable_count += 1
    else:
      raise ValueError("Object has never did undo: {:s}".format(repr(self)))
