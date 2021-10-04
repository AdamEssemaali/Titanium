import subprocess


class TitaniumRunner:
    def __init__(self,cfile,output) -> None:
        self.cfile = cfile
        self.output = output
    def compile(self):
        print("Compiling...")
        subprocess.call(["g++", self.cfile, "-o", self.output])
        print("Program compiled successfuly")