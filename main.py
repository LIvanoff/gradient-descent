from freader.fread import fread
from visualization.visualizator import visualizator
import subprocess

program = "C:/Users/drfri/source/repos/Optimizer/x64/Debug/Optimizer.exe"
process = subprocess.Popen(program)
code = process.wait()

visualizator(fread('./coordinates.txt'))