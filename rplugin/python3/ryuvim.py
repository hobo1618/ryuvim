import pynvim
from pathlib import Path

# from openai import OpenAI
import os

# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
# raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Set up the API request to OpenAI
# client = OpenAI(api_key=api_key)


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("ryuvim").getConfig()')
        print("Hello Init!")

    @pynvim.function("Ryuvim", sync=True)
    def ryuvim(self):
        self.nvim.command('echo "Hello World!"')
        print("Hello World print!")

    @pynvim.command("RyuvimCommand", nargs="*")
    def ryuvim_command(self):
        # self.nvim.command('echo "Hello command!"')
        print("Hello command print!")

    @pynvim.function("TestFunction", sync=True)
    def testfunction(self, args):
        return 3

    @pynvim.command("TestCommand", nargs="*", range="")
    def testcommand(self, args, range):
        self.nvim.current.line = "Command with args: {}, range: {}".format(args, range)

    @pynvim.autocmd("BufEnter", pattern="*.py", eval='expand("<afile>")', sync=True)
    def on_bufenter(self, filename):
        self.nvim.out_write("testplugin is in " + filename + "\n")

    # @pynvim.function("RyuvimOpenAI", sync=True)
    # def ryuvimOpenAI(self):
    #     response = client.chat.completions.create(
    #         model="gpt-4o",
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {
    #                 "role": "user",
    #                 "content": "Give me a good recipe for homemade pasta.",
    #             },
    #         ],
    #     )
    #     content = response.choices[0].message.content
    #     if not content:
    #         raise ValueError("No content returned from OpenAI.")
    #
    #     self.nvim.command('echo "{}"'.format(content))
    #     print("Hello Worldsss!")
