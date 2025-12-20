
# undoable

## Overview

![](https://img.shields.io/badge/Python-3.12-blue)
![](https://img.shields.io/badge/License-AGPLv3-blue)

アンドゥ・リドゥ機能を提供します。

GUIアプリケーションを作成するにあたり、アンドゥ・リドゥ機能が必要になったため作成しました。
主な機能としては、アンドゥ・リドゥそのものに加えて、アンドゥ・リドゥ操作が可能かどうかを判定する機能、値を確定し変更履歴を削除する機能などがあります。

## Usage

基本機能の実行例

```py
from undoable import Undoable

ud = Undoable(1)

ud.set(2)
ud.get() #2

ud.undo()
ud.get() #1

ud.redo()
ud.get() #2
```

値を確定し変更履歴を削除する実行例

```py
from undoable import Undoable

ud = Undoable(1)

ud.set(2)
ud.get() #2
ud.can_undo #True

ud.fix()
ud.get() #2
ud.can_undo #False
```

## Install

```shell
pip install .
```

### Test

```shell
pip install .[test]
pytest .
```

### Document

```py
import undoable

help(undoable)
```

## Donation

<a href="https://buymeacoffee.com/tikubonn" target="_blank"><img src="doc/img/qr-code.png" width="3000px" height="3000px" style="width:150px;height:auto;"></a>

もし本パッケージがお役立ちになりましたら、少額の寄付で支援することができます。<br>
寄付していただいたお金は書籍の購入費用や日々の支払いに使わせていただきます。
ただし、これは寄付の多寡によって継続的な開発やサポートを保証するものではありません。ご留意ください。

If you found this package useful, you can support it with a small donation.
Donations will be used to cover book purchases and daily expenses.
However, please note that this does not guarantee ongoing development or support based on the amount donated.

## License

© 2025 tikubonn

undoable licensed under the [AGPLv3](./LICENSE).
