import sys
import re

help_text = """
Welcome to WPython.

Args:

  --debug        Debug mode
  --print-words  Prints all abbreviated keywords
  --to-wpy       Translation mode from py to wpy
  --save-file    Save file after processing
  --auto-exec    Execute output if is possible

Usage:
wpython.exe <file> <args>
"""

keywords_dict = {
    "False": "F",
    "None": "N",
    "True": "T",
    "and": "a",
    "as": "as",
    "assert": "asrt",
    "async": "ayc",
    "await": "awt",
    "break": "brk",
    "class": "cls",
    "continue": "cnt",
    "def": "df",
    "del": "dl",
    "elif": "el",
    "else": "es",
    "except": "ex",
    "finally": "fnl",
    "for": "fr",
    "from": "fm",
    "global": "glb",
    "if": "if",
    "import": "imp",
    "in": "in",
    "is": "is",
    "lambda": "lb",
    "nonlocal": "nl",
    "not": "nt",
    "or": "or",
    "pass": "ps",
    "raise": "rs",
    "return": "rt",
    "try": "tr",
    "while": "wh",
    "with": "wth",
    "yield": "yd",
    "print": "prt",
    "input": "inp"
}

is_debug_mode = False
save_file = False
to_wpy_mode = False
auto_exec = False

def process_args(args: list):
    global is_debug_mode, keywords_dict, save_file, to_wpy_mode, auto_exec

    for _raw_arg in args:
        raw_arg = str(_raw_arg)

        if raw_arg.startswith("--"):
            arg = raw_arg.replace("--", "")

            if arg == "debug":
                is_debug_mode = True
            elif arg == "print-words":
                print(f"{'Original'.ljust(12)}Abbreviated")
    
                for original, abbreviated in keywords_dict.items():
                    print(f"{original.ljust(12)}{abbreviated}")
                sys.exit(0)
            elif arg == "save-file":
                save_file = True
            elif arg == "to-wpy":
                to_wpy_mode = True
            elif arg == "auto-exec":
                auto_exec = True

def log(message: str = ""):
    global is_debug_mode
    if is_debug_mode:
        print(f"• {message}")

def preprocess(file_name: str):
    global save_file, to_wpy_mode
    log("Starting preprocessing...")
    raw_lines = ""
    processed_lines = ""

    log(f"  Opening {file_name}...")
    try:
        with open(file_name, "r") as file:
            log(f"  Reading {file_name}...")
            raw_lines = file.readlines()
    except Exception as e:
        print("• Exception in preprocessing: " + str(e))
        sys.exit(0)

    sentence = "Python to WPython" if to_wpy_mode else "WPython to Python"
    log(f"  Starting to translate {sentence}...")

    for line in raw_lines:
        original_line = line

        def replace_keyword(match):
            word = match.group(0)
            for original, abbr in keywords_dict.items():
                if word == abbr and not to_wpy_mode:
                    return original
                elif word == original:
                    return abbr
            return word

        regex = r'\b\w+\b(?=(?:[^"]*"[^"]*")*[^"]*$)'
        processed_line = re.sub(regex, replace_keyword, line)

        log(f"    Original: {original_line.strip()}")
        log(f"    Processed: {processed_line.strip()}")

        processed_lines += processed_line

    log("  Translation completed")
    log()

    if not to_wpy_mode and save_file or to_wpy_mode:
        log("  Saving output file...")
        extension = "wpy" if to_wpy_mode else "py"
        with open(f"output.{extension}", "w") as file:
            log("  Writing lines...")
            file.write(processed_lines)
            log("  Saved")
        
        if to_wpy_mode:
            sys.exit(0)

    return processed_lines

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print(help_text)
        sys.exit(0)

    process_args(args)

    to_exec = preprocess(args[1])

    if auto_exec:
        log()
        log("Executing...")

        exec(to_exec)