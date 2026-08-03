# -*- coding: utf-8 -*-
"""
Converted from IPYNB to PY
"""

# %% [code] Cell 1
import gradio as gr
import numpy as np
import matplotlib.pyplot as plt

# Global variables
x = None
y = None


def generate_points(n_points):
    global x, y

    x = np.sort(np.random.uniform(0, 10, n_points))

    true_slope = np.random.uniform(0.5, 3.5)
    true_intercept = np.random.uniform(-2, 4)

    noise = np.random.normal(0, 1, n_points)

    y = true_slope * x + true_intercept + noise

    fig, ax = plt.subplots(figsize=(6,5))
    ax.scatter(x, y, color="blue")
    ax.set_title("Random Data")
    ax.grid(True)

    return fig, "Points Generated!"


def update_line(slope, intercept):
    global x, y

    if x is None:
        return None, "Generate points first."

    y_pred = slope * x + intercept

    mse = np.mean((y - y_pred) ** 2)

    fig, ax = plt.subplots(figsize=(6,5))

    ax.scatter(x, y, color="blue", label="Data")
    ax.plot(x, y_pred, color="red", linewidth=3, label="Regression Line")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Linear Regression")
    ax.grid(True)
    ax.legend()

    return fig, f"### MSE = {mse:.4f}"


with gr.Blocks(title="Linear Regression Demo") as demo:

    gr.Markdown("# Linear Regression Visualizer")

    with gr.Row():
        num_points = gr.Number(value=30, label="Number of Points")

        generate_btn = gr.Button("Generate Random Points")

    plot = gr.Plot()

    status = gr.Markdown("")

    slope = gr.Slider(
        minimum=-10,
        maximum=10,
        value=1,
        step=0.1,
        label="Slope (θ₀)"
    )

    intercept = gr.Slider(
        minimum=-10,
        maximum=10,
        value=0,
        step=0.1,
        label="Intercept (θ₁)"
    )

    generate_btn.click(
        generate_points,
        inputs=num_points,
        outputs=[plot, status]
    )

    slope.change(
        update_line,
        inputs=[slope, intercept],
        outputs=[plot, status]
    )

    intercept.change(
        update_line,
        inputs=[slope, intercept],
        outputs=[plot, status]
    )

if __name__ == "__main__":
    demo.launch(share=True)
