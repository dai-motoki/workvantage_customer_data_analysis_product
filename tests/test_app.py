# 上記の内容をもとにしてapp.pyに対するユニットテストを作成するには、Python のユニットテストフレームワークである unittest を使用することができます。以下は、app.pyに対するユニットテストの例です:
# 
import unittest
from app import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 10), -10)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
# 
# このテストケースでは、以下のことをチェックしています:
# 
# 1. `add()` 関数が正常に動作すること
# 2. `subtract()` 関数が正常に動作すること
# 3. `multiply()` 関数が正常に動作すること
# 4. `divide()` 関数が正常に動作し、0による除算エラーが発生すること
# 
# テストを実行するには、以下のコマンドを実行します:
# 
# python test_app.py
# 
# これにより、すべてのテストケースが成功することを確認できます。ユニットテストを書くことで、アプリケーションの品質を保ち、将来の変更による影響を最小限に抑えることができます。