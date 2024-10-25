import pynvim
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Set up the API request to OpenAI
client = OpenAI(api_key=api_key)


@pynvim.plugin
class Ryuvim(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("Ryuvim", nargs="*")
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
