import pynvim


print("Back end is running from /backend/main.py")


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("Ryuvim", nargs="*")
    def ryuvim(self, args):
        self.nvim.command('echo "Hello World!"')
        print("Hello World!")
        print(args)
