import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#20232a")

        self.entries = []
        self.solution = []
        self.puzzle = []

        self.create_ui()
        self.new_game()

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="SUDOKU GAME",
            font=("Arial", 24, "bold"),
            bg="#20232a",
            fg="white"
        )
        title.pack(pady=15)

        self.board_frame = tk.Frame(self.root, bg="white")
        self.board_frame.pack(pady=10)

        for row in range(9):
            row_entries = []

            for col in range(9):

                entry = tk.Entry(
                    self.board_frame,
                    width=2,
                    font=("Arial", 18, "bold"),
                    justify="center",
                    bd=1,
                    relief="solid"
                )

                entry.grid(
                    row=row,
                    column=col,
                    ipady=8,
                    padx=(2 if col % 3 == 0 else 0),
                    pady=(2 if row % 3 == 0 else 0)
                )

                row_entries.append(entry)

            self.entries.append(row_entries)

        button_frame = tk.Frame(self.root, bg="#20232a")
        button_frame.pack(pady=20)

        buttons = [
            ("Check", self.check_answer),
            ("Hint", self.give_hint),
            ("Reset", self.reset_game),
            ("New Game", self.new_game)
        ]

        for text, command in buttons:
            tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 10, "bold"),
                bg="#61dafb",
                fg="black",
                padx=10,
                pady=8
            ).pack(side="left", padx=5)

        self.status = tk.Label(
            self.root,
            text="Fill the empty cells!",
            font=("Arial", 12),
            bg="#20232a",
            fg="white"
        )
        self.status.pack(pady=10)

    def is_valid(self, board, row, col, num):

        for i in range(9):
            if board[row][i] == num:
                return False

            if board[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(self, board):

        for row in range(9):
            for col in range(9):

                if board[row][col] == 0:

                    for num in range(1, 10):

                        if self.is_valid(board, row, col, num):

                            board[row][col] = num

                            if self.solve(board):
                                return True

                            board[row][col] = 0

                    return False

        return True

    def generate_puzzle(self):

        board = [[0 for _ in range(9)] for _ in range(9)]

        self.solve(board)

        self.solution = [row[:] for row in board]

        puzzle = [row[:] for row in board]

        cells = list(range(81))
        random.shuffle(cells)

        for cell in cells[:40]:
            row = cell // 9
            col = cell % 9
            puzzle[row][col] = 0

        self.puzzle = [row[:] for row in puzzle]

    def new_game(self):

        self.generate_puzzle()

        for row in range(9):
            for col in range(9):

                entry = self.entries[row][col]
                entry.config(state="normal")
                entry.delete(0, tk.END)

                value = self.puzzle[row][col]

                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(
                        state="readonly",
                        readonlybackground="#d6eaf8",
                        fg="#17202a"
                    )
                else:
                    entry.config(
                        bg="white",
                        fg="black"
                    )

        self.status.config(text="New game started!")

    def check_answer(self):

        correct = True
        empty = False

        for row in range(9):
            for col in range(9):

                value = self.entries[row][col].get()

                if not value:
                    empty = True
                    continue

                if not value.isdigit() or not (1 <= int(value) <= 9):
                    self.status.config(text="Enter numbers from 1 to 9!")
                    return

                if int(value) != self.solution[row][col]:
                    correct = False
                    self.entries[row][col].config(bg="#ffcccc")
                else:
                    self.entries[row][col].config(bg="#d5f5e3")

        if correct and not empty:
            self.status.config(text="Congratulations! You won!")
            messagebox.showinfo("Winner", "Sudoku completed successfully!")
        elif not correct:
            self.status.config(text="Some answers are incorrect!")
        else:
            self.status.config(text="Keep going! Some cells are empty.")

    def give_hint(self):

        empty_cells = []

        for row in range(9):
            for col in range(9):

                if self.entries[row][col].get() == "":
                    empty_cells.append((row, col))

        if not empty_cells:
            messagebox.showinfo("Hint", "No empty cells!")
            return

        row, col = random.choice(empty_cells)

        entry = self.entries[row][col]
        entry.insert(0, str(self.solution[row][col]))
        entry.config(bg="#d5f5e3")

        self.status.config(text="Hint added!")

    def reset_game(self):

        for row in range(9):
            for col in range(9):

                entry = self.entries[row][col]

                if self.puzzle[row][col] == 0:
                    entry.delete(0, tk.END)
                    entry.config(bg="white")

        self.status.config(text="Game reset!")


if __name__ == "__main__":

    root = tk.Tk()

    game = SudokuGame(root)

    root.mainloop()
