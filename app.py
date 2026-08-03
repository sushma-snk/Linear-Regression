import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Regression Visualizer",
    layout="wide"
)

st.title("📈 Linear Regression Visualizer")

st.write(
    """
Adjust the slope (θ₀) and intercept (θ₁) to fit the regression line
to the generated dataset.
"""
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "x" not in st.session_state:

    st.session_state.x = None
    st.session_state.y = None
    st.session_state.true_slope = None
    st.session_state.true_intercept = None

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.header("Dataset")

num_points = st.sidebar.number_input(
    "Number of Points",
    min_value=5,
    max_value=500,
    value=30
)

if st.sidebar.button("Generate Random Dataset"):

    np.random.seed()

    x = np.sort(np.random.uniform(0,10,num_points))

    true_slope = np.random.uniform(0.5,3.5)

    true_intercept = np.random.uniform(-2,4)

    noise = np.random.normal(0,1,num_points)

    y = true_slope*x + true_intercept + noise

    st.session_state.x = x
    st.session_state.y = y

    st.session_state.true_slope = true_slope
    st.session_state.true_intercept = true_intercept

# ----------------------------------------------------
# Sliders
# ----------------------------------------------------

theta0 = st.sidebar.slider(
    "Slope (θ₀)",
    -10.0,
    10.0,
    1.0,
    0.1
)

theta1 = st.sidebar.slider(
    "Intercept (θ₁)",
    -10.0,
    10.0,
    0.0,
    0.1
)

# ----------------------------------------------------
# Plot
# ----------------------------------------------------

if st.session_state.x is not None:

    x = st.session_state.x
    y = st.session_state.y

    y_pred = theta0*x + theta1

    mse = np.mean((y-y_pred)**2)

    col1,col2 = st.columns([3,1])

    with col1:

        fig,ax = plt.subplots(figsize=(8,6))

        ax.scatter(
            x,
            y,
            color="royalblue",
            s=50,
            label="Random Points"
        )

        ax.plot(
            x,
            y_pred,
            color="crimson",
            linewidth=3,
            label="Regression Line"
        )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        ax.set_title("Linear Regression")

        ax.grid(True)

        ax.legend()

        st.pyplot(fig)

    with col2:

        st.metric(
            "Mean Squared Error",
            f"{mse:.4f}"
        )

        st.markdown("### Current Equation")

        st.latex(
            rf"y={theta0:.2f}x+{theta1:.2f}"
        )

        st.markdown("### Hidden True Equation")

        st.latex(
            rf"y={st.session_state.true_slope:.2f}x+{st.session_state.true_intercept:.2f}"
        )

else:

    st.info("Click **Generate Random Dataset** to begin.")
