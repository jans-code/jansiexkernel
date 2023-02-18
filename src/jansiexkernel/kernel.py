#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

def rm_line(solution):
    solution = solution.split("\n")
    ret_val = ""
    for i in range(len(solution)-1):
        ret_val = ret_val + solution[i] + "\n"
    return ret_val

iexwrapper = replwrap.REPLWrapper("iex", ")>", None)

class jansiexkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'iex'
    language_version = '1.14.0'
    language_info = {
        'name': 'iex',
        'mimetype': 'application/elixir',
        'file_extension': '.ex',
    }
    banner = "iex - mixing Elixir in the shell!"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            code = code.replace("\n"," ")
            solution = iexwrapper.run_command(code)
            solution = rm_line(solution)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
