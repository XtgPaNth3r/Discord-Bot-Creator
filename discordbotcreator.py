print('Type helpme for help on the commands! Use the draganddrop.py file to help by ordering the blocks around.')
def read_code():
    with open('code.py', 'r') as f:
        return f

def wc(write):
    with open('code.py', 'a') as f:
        f.write(write)

def nl():
    wc('\n')


imports = """
import discord
from discord.ext import commands
"""


while True:
    op = input('What would you like to do? ').lower()
    if op == 'r':
        import code

        
    elif op == 'i':
        wc(imports)

        
    elif op == 'p':
        pre = input('What is the prefix? ').lower()
        wc(f'client = command.Bot(command_prefix=\'{pre}\')')
        nl()

        
    elif op == 'c':
        cmdn = input('What is the name of the command? ').lower()
        wc('@client.commands()')
        nl()
        wc(f'async def {cmdn}(ctx):')
        nl()
        inc = input('What would you like to put in the command? ').lower()
        if inc == 'say':
            say = input('What would you like to say? ')
            wc(f'   await ctx.send(\'{say}\')')
            nl()

            
    elif op == 'clear':
        with open('code.py', 'w') as f:
            f.write('')

            
    elif op == 't':
        token = input('What is the bot token? ')
        wc(f'client.run(\'{token}\')')
    elif op == 'd':
        print('Play p1 then p2.mp4')

    elif op == 'custom':
            print('Go into code.py to write custom code.')

    elif op == 'mycode':
        with open('code.py', 'r') as f:
            c = f.read()
        print(c)
        
    elif op == 'helpme':
        print("""r = Run
i = import default modules
p = set command prefix
c = new command
s = say
t = token
clear = clear code
d = demonstration
custom = custom code
mycode = get your code
q = quit""")

        
    else:
        print('Not valid!')
