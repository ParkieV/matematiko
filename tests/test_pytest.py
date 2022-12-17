import sys
sys.path.insert(0, "C:/projects/matematiko")
from Game import Game


def test_game_logic1():
    player = Game()
    player.add(0, 0, 1)
    player.add(0, 1, 1)
    player.add(0, 2, 1)
    player.add(0, 3, 1)
    assert player.acc == 200

    player.add(1, 0, 1)
    player.add(1, 1, 1)
    player.add(1, 2, 1)
    player.add(1, 3, 1)
    assert player.acc == 460
    
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 1)
    player.add(2, 3, 13)
    player.add(2, 4, 13)
    assert player.acc == 700

def test_game_logic2():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 0)
    player.add(2, 3, 13)
    player.add(2, 4, 13)
    assert player.acc == 20

def test_game_logic3():
    player = Game()
    player.add(0, 0, 3)
    player.add(1, 1, 3)
    player.add(2, 2, 2)
    player.add(3, 3, 13)
    player.add(4, 4, 13)
    assert player.acc == 30

def test_game_logic4():
    player = Game()
    player.add(2, 0, 3)
    player.add(2, 1, 3)
    player.add(2, 2, 2)
    player.add(2, 3, 13)
    player.add(2, 4, 13)
    assert player.acc == 20
    
def test_game_logic5():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 5)
    player.add(2, 3, 6)
    player.add(2, 4, 7)
    assert player.acc == 10

    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 0)
    player.add(2, 3, 0)
    player.add(2, 4, 0)
    assert player.acc == 10
    
def test_game_logic6():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 1)
    player.add(2, 3, 6)
    player.add(2, 4, 7)
    assert player.acc == 40
    
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 1)
    player.add(2, 3, 0)
    player.add(2, 4, 0)
    assert player.acc == 40

def test_game_logic7():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 1)
    player.add(2, 2, 1)
    player.add(2, 3, 1)
    player.add(2, 4, 7)
    assert player.acc == 200
    
    player.add(2, 0, 2)
    player.add(2, 1, 2)
    player.add(2, 2, 2)
    player.add(2, 3, 2)
    player.add(2, 4, 0)
    assert player.acc == 160

def test_game_logic8():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 5)
    player.add(2, 2, 3)
    player.add(2, 3, 4)
    player.add(2, 4, 2)
    assert player.acc == 50

def test_game_logic9():
    player = Game()
    player.add(2, 0, 1)
    player.add(2, 1, 12)
    player.add(2, 2, 11)
    player.add(2, 3, 10)
    player.add(2, 4, 13)
    assert player.acc == 150

def test_game_logic10():
    player = Game()
    player.add(0, 0, 2)
    player.add(1, 1, 2)
    player.add(2, 2, 2)
    player.add(3, 3, 13)
    player.add(4, 4, 13)
    assert player.acc == 90