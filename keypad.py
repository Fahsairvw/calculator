import tkinter as tk


class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i in range(len(self.keynames)):
            col = i % columns
            row = i // columns
            button = tk.Button(self, text=str(self.keynames[i]))
            button.grid(row=row, column=col, padx=2, pady=2, sticky=tk.NSEW)
            button['bg'] = 'black'

        for j in range(row+1):
            self.rowconfigure(j, weight=1)
        for i in range(columns):
            self.columnconfigure(i, weight=1)

    def bind(self, todo, function):
        """Bind an event handler to an event sequence."""
        for i in self.winfo_children():
            i.bind(todo, function)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for i in self.winfo_children():
            i[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        widget = self.winfo_children()[0]
        return widget[key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        self.frame.configure(cnf=cnf, **kwargs)

    @property
    def frame(self):
        return super()
