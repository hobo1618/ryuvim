import pynvim


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("Ryu", nargs="*", range="")
    def ryu(self, args, range):
        self.nvim.command("echo 'Ryu is the best!'")
