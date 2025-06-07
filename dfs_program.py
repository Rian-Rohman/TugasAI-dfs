import tkinter as tk
import time

SIZE = 5  # ukuran grid 5x5
DELAY = 0.5  # jeda waktu antar langkah (detik)

class DFSVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("DFS Q1-Q5 Visualizer")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.solution = [-1] * SIZE
        self.running = False
        self.cells = [[None]*SIZE for _ in range(SIZE)]

        self.draw_grid()
        btn = tk.Button(root, text="Mulai DFS", command=self.start_dfs)
        btn.pack(pady=10)

    def draw_grid(self):
        cell_size = 60
        for i in range(SIZE):
            for j in range(SIZE):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.cells[i][j] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                self.canvas.create_text(x1 + 30, y1 + 30, text=f"{i+1}.{j+1}", tags=f"text_{i}_{j}")

    def update_cell(self, row, col, label, color):
        self.canvas.itemconfig(self.cells[row][col], fill=color)
        self.canvas.delete(f"label_{row}_{col}")
        self.canvas.create_text(col * 60 + 30, row * 60 + 30, text=label, fill="black", font=("Arial", 12, "bold"), tags=f"label_{row}_{col}")
        self.root.update()
        time.sleep(DELAY)

    def clear_label(self, row, col):
        self.canvas.itemconfig(self.cells[row][col], fill="white")
        self.canvas.delete(f"label_{row}_{col}")
        self.root.update()
        time.sleep(DELAY)

    def is_safe(self, solution, row, col):
        for r in range(row):
            c = solution[r]
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def dfs(self, row):
        if row == SIZE:
            return True  # Solusi ditemukan
        for col in range(SIZE):
            if self.is_safe(self.solution, row, col):
                self.solution[row] = col
                self.update_cell(row, col, f"q{row+1}", "lightgreen")
                if self.dfs(row + 1):
                    return True
                # Backtrack
                self.solution[row] = -1
                self.clear_label(row, col)
        return False

    def start_dfs(self):
        if not self.running:
            self.running = True
            self.dfs(0)

# Buat GUI
root = tk.Tk()
app = DFSVisualizer(root)
root.mainloop()
