import pynvim
from pathlib import Path
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Set up the API request to OpenAI
client = OpenAI(api_key=api_key)


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("ryuvim").getConfig()')
        self.path = Path(self.cfg["path"]).expanduser()

    @pynvim.function("Ryuvim")
    def ryuvim(self):
        self.nvim.command('echo "Hello World!"')
        print("Hello World!")

    @pynvim.function("RyuvimOpenAI")
    def ryuvimOpenAI(self):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "Give me a good recipe for homemade pasta.",
                },
            ],
        )
        content = response.choices[0].message.content
        if not content:
            raise ValueError("No content returned from OpenAI.")

        self.nvim.command('echo "{}"'.format(content))
        print("Hello Worldsss!")
