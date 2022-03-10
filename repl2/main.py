# Repl for fun
import datetime as dt
import platform as pl

# Constants
VAR_VERSION = 'REPL v0.1.1'
HEADER = "Welcome to REPL, type 'help' for command list, 'exit' for exit from REPL"
FOOTER = "Thanks for using REPL!"
PROMPT_COMMAND = ": "
PROMPT_ECHO = ">> "
PROMPT_ERROR = "Error: "

# Message strings
MSG_ECHO_ON = 'Echo mode is on'
MSG_ECHO_OFF = 'Echo mode is off'

# Error string
ERR_WRONG_COMMAND = 'Wrong command: {0}'
ERR_COMMAND_EXEC = 'Command execution error'

# System Commands
CMD_EXIT = 'exit'
CMD_ECHO_ON = 'echo_on'
CMD_ECHO_OFF = 'echo_off'
CMD_HELP = 'help'

# Commands
CMD = ['hello_world', 'current_date', 'current_time', 'current_datetime', 'version', 'osname']

# ToDo
# + time
# + version
# + osname
# - parameters
# - echo
# - memory: processes, kill
# - repl: history, last, variables, pipe
# - fs: cwd, ls, cd, cp, rn, rm
# - cat
# - calc
# - exec
# - exec on background and internal processes
# - network
# - client-server connection


# Building commands
def cmd_hello_world():
    print("HELLO WORLD")


def cmd_current_date():
    print('{0}{1}'.format(PROMPT_ECHO, dt.datetime.now().date()))


def cmd_current_time():
    print('{0}{1}'.format(PROMPT_ECHO, dt.datetime.now().time()))


def cmd_current_datetime():
    print('{0}{1}'.format(PROMPT_ECHO, dt.datetime.now().today()))


def cmd_version():
    print('{0}{1}'.format(PROMPT_ECHO, VAR_VERSION))


def cmd_osname():
    print('{0}{1}'.format(PROMPT_ECHO, pl.system() + ' ' + pl.release()))


# Main block
def main():
    # System Variables
    var_echo = False

    # Header for REPL
    print(HEADER)

    # Infinite loop
    while True:
        # Get command from console
        rep = input(PROMPT_COMMAND)

        # echo mode
        if var_echo: print('{0}{1}'.format(PROMPT_ECHO, rep))

        # exit command
        if rep == CMD_EXIT:
            break
        else:
            # Command Processor

            # System Command
            # echo_on command
            if rep == CMD_ECHO_ON:
                var_echo = True
                print(MSG_ECHO_ON)

            # echo_off command
            elif rep == CMD_ECHO_OFF:
                var_echo = False
                print(MSG_ECHO_OFF)

            # help command
            elif rep == CMD_HELP:
                for c in CMD:
                    print(c)

            # Building commands
            elif rep in CMD:
                try:
                    eval('cmd_' + rep + '()')
                except:
                    print(PROMPT_ERROR + ERR_COMMAND_EXEC)

            # Command not found
            else: print(ERR_WRONG_COMMAND.format(rep))

    # Footer for repl
    print(FOOTER)


if __name__ == '__main__':
    main()




