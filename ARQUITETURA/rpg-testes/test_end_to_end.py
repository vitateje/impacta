import os
import subprocess
from subprocess import PIPE

def test_guerreiro_parm():
    #arrange
    expectation = f'atacando: pot: 33, dis: 1, dir: frente{os.linesep}'
    
    #act
    path = os.path.dirname(os.path.realpath(__file__))
    with subprocess.Popen(["python3", "app.py", "Guerreiro"], cwd=path, stdout=PIPE) as p:
        result = p.stdout.read()

    #assert
    assert result.decode("utf-8") == expectation
