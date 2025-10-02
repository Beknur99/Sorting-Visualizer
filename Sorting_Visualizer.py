import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Bubble Sort algorithm with step visualization
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data

# Generate a random array
N = 20
data = [random.randint(1, 50) for _ in range(N)]
generator = bubble_sort(data)

# Set up the plot
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), data, align="edge")
ax.set_xlim(0, N)
ax.set_ylim(0, int(max(data)) + 1)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]

def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"Iterations: {iteration[0]}")

anim = animation.FuncAnimation(
    fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator, interval=200, repeat=False
)

plt.show()
