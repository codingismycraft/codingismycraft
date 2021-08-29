import unittest
import my_bfs

class Test_my_bfs(unittest.TestCase):

    def test_my_bfs(self):
        data = {
            '0': ['1', '2'],
            '1': ['0', '3', '4'],
            '2': ['0'],
            '3': ['1'],
            '4': ['2', '3']
        }
        print(my_bfs.bfs(data,"0","3"))
        print(my_bfs.bfs(data, "0", "2"))
        print(my_bfs.bfs(data, "0", "32"))

if __name__ == '__main__':
    unittest.main()

