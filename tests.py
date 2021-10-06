#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 10
day = 8

def test_code():
    assert main.countA("rat") == 1, "countA('rat') == 1 failed"
    assert main.countA("oooooooo") == 0, "countA('oooooooo') == 0 failed"
    assert main.countA("aaaaaaaaaa") == 10, "countA('aaaaaaaaaa') == 10 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
