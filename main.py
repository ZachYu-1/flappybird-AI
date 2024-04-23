import tkinter as tk
import runpy

scripts = {
    'Run Q-Learning': 'flappy_rl',
    'Run NEAT': 'run_neat',
}


def run_script(script_name, root):
    try:
        runpy.run_module(script_name, run_name="__main__")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_button(window, text, script_name):
    return tk.Button(window, text=text, command=lambda: run_script(script_name, window), height=2, width=20)


def main():
    root = tk.Tk()
    root.title("Script Runner")
    for text, script_name in scripts.items():
        button = create_button(root, text, script_name)
        button.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    main()