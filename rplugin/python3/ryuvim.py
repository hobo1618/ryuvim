import pynvim
from pathlib import Path


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("ryuvim").getConfig()')
        self.path = Path(self.cfg["path"]).expanduser()

    @pynvim.function("Ryuvim")
    def ryuvim(self, args):
        self.nvim.command('echo "Hello World!"')
        print("Hello World!")
        print(args)

    # @pynvim.command("RyuvimOpenAI", nargs="*")
    # def ryuvimOpenAI(self, args):
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
