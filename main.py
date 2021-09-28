import sys, os
import subprocess as sp

platform = sys.platform

game = input('Você quer jogar um jogo? ')
if (game == "sim"):
    if ("win" in platform):
        os.startfile("https://brunolemos.github.io/trust/")
    elif ("linux" in platform):
        try:
            sp.Popen("https://brunolemos.github.io/trust/")
        except FileNotFoundError:
            sp.Popen("xdg-open", "https://brunolemos.github.io/trust/")



