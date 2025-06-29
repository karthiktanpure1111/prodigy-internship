import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, width=2, font=("Arial", 18), justify='center')
                entry.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 0), pady=(2 if i % 3 == 0 else 0))
                self.entries[i][j] = entry

                # Bind Enter key to jump to next cell
                entry.bind("<Return>", lambda event, row=i, col=j: self.focus_next_cell(row, col))

    def focus_next_cell(self, row, col):
        next_col = col + 1
        next_row = row

        if next_col >= 9:
            next_col = 0
            next_row += 1

        if next_row < 9:
            self.entries[next_row][next_col].focus_set()

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        solve_btn = tk.Button(button_frame, text="Solve", command=self.solve_sudoku,
                              font=("Arial", 14), bg="lightgreen", width=10)
        solve_btn.grid(row=0, column=0, padx=10)

        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_board,
                              font=("Arial", 14), bg="lightcoral", width=10)
        clear_btn.grid(row=0, column=1, padx=10)

    def get_board(self):
        board = []
        for row in self.entries:
            current_row = []
            for cell in row:
                val = cell.get()
                current_row.append(int(val) if val.isdigit() else 0)
            board.append(current_row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)

    def solve_sudoku(self):
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)
            messagebox.showinfo("Solved", "Sudoku solved successfully!")
        else:
            messagebox.showerror("Error", "No solution exists.")

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

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
