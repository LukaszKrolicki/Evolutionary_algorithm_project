import os
import numpy as np
from matplotlib import pyplot as plt, animation
from optimization_functions import martin_gaddy
os.makedirs("results", exist_ok=True)

def generate_plots(history, best_solution, fit_hist, operations, begin_range, end_range):
    x = np.linspace(begin_range, end_range, 100)
    y = np.linspace(begin_range, end_range, 100)
    X, Y = np.meshgrid(x, y)
    Z = martin_gaddy(X, Y)

    # 3D Surface Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    # Plot best solution
    ax.scatter(best_solution[0], best_solution[1], martin_gaddy(*best_solution), c='r', marker='o', s=100,
               label=f'Best Solution ({best_solution[0]:.2f}, {best_solution[1]:.2f})')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.view_init(elev=25, azim=35)
    ax.set_title("3D Plot z najlepszym rozwiązaniem")
    plt.legend()
    plt.savefig("results/3d_plot.png")
    plt.close()

    # Heatmap
    plt.figure()
    plt.contourf(X, Y, Z, cmap='hot', levels=50)
    plt.colorbar()
    plt.scatter(best_solution[0], best_solution[1], c='blue', marker='x', s=100,
                label=f'Najlepsze rozwiązanie ({best_solution[0]:.2f}, {best_solution[1]:.2f})')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Najlepsze rozwiązanie")
    plt.legend()
    plt.savefig("results/heatmap.png")
    plt.close()

    # Animation
    fig, ax = plt.subplots()
    ax.set_xlim(begin_range, end_range)
    ax.set_ylim(begin_range, end_range)
    ax.set_title("Przebieg znalezienia najlepszego rozwiązania")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.contourf(X, Y, Z, cmap='hot', levels=50)

    scatter = ax.scatter([], [], c='red', s=50)

    def update(frame):
        ax.set_title("Przebieg znalezienia najlepszego rozwiązania" + f" (Epoch {frame + 1})")
        scatter.set_offsets(history[:frame + 1])
        return scatter,

    ani = animation.FuncAnimation(fig, update, frames=len(history), interval=200, blit=True)
    ani.save("results/evolution.gif", writer='pillow')
    plt.close()

    # Fitness over iterations plot
    plt.figure(figsize=(10, 6))
    iterations = list(range(1, len(history) + 1))
    fitness_values = [point[1] for point in history]

    plt.plot(iterations, fitness_values, 'b-', linewidth=2)
    plt.scatter(iterations, fitness_values, c='blue', s=30)

    plt.xlabel("Iteracja")
    plt.ylabel("Wartość fitness")
    plt.title("Wartość fitness w kolejnych iteracjach")
    plt.grid(True, linestyle='--', alpha=0.7)

    # Add annotation for the best fitness value
    best_iteration = fit_hist.index(min(fit_hist)) + 1
    best_fitness = min(fit_hist)
    plt.annotate(f'Najlepsze dopasowanie: {best_fitness:.6f}',
                 xy=(best_iteration, best_fitness),
                 xytext=(best_iteration + len(iterations) // 10, best_fitness * 1.1),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
                 fontsize=10)

    plt.tight_layout()
    plt.savefig("results/fitness_plot.png")
    plt.close()

    # Event log
    with open("results/event_log.txt", "w") as f:
        f.write("Epoch\tEvent\tDetails\n")

        last_epoch = -1
        for entry in operations:
            epoch = entry.get('epoch', 'N/A')
            event = entry.get('type', 'N/A')

            if epoch != last_epoch:
                f.write("\n")
                last_epoch = epoch

            if event in ['selection', 'crossover','result children']:
                details = f"({entry['parents'][0]}, {entry['parents'][1]})" if 'parents' in entry else f"({entry['children'][0]}, {entry['children'][1]})"
            elif event == 'mutation' or event == 'inversion':
                details = f"{entry['child']}"
            elif event in ['initial_population', 'final_population']:
                details = "\n".join([f"({x[0]}), Fitness: {x[1]}" for x in entry['population']])
            else:
                details = "No details available"

            f.write(f"{epoch}\t{event}\t{details}\n")

def save_results(best_solution, history, fit_hist, operations, begin_range, end_range):
    generate_plots(history, best_solution, fit_hist, operations, begin_range, end_range)
    print("Wyniki zapisane w folderze 'results'")