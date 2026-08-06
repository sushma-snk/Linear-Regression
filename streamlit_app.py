# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# # ---------------------------------------------------------
# # Page Configuration
# # ---------------------------------------------------------
# st.set_page_config(
#     page_title="Linear Regression Visualizer",
#     page_icon="📈",
#     layout="wide"
# )

# st.title("📈 Linear Regression Visualizer")
# st.write(
#     """
# This interactive application demonstrates how the **Slope (θ₀)** and
# **Intercept (θ₁)** affect the regression line and the corresponding
# **Mean Squared Error (MSE)**.

# ### Instructions
# 1. Select the number of random points.
# 2. Click **Generate Random Dataset**.
# 3. Adjust the sliders to fit the regression line.
# 4. Observe how the **MSE** changes.
# 5. Click **Reveal True Equation** to compare your estimate.
# """
# )

# # ---------------------------------------------------------
# # Session State
# # ---------------------------------------------------------    
# # if "x" not in st.session_state:
# #     st.session_state.x = None
# #     st.session_state.y = None
# #     st.session_state.true_slope = None
# #     st.session_state.true_intercept = None

# # ---------------------------------------------------------
# # Session State
# # ---------------------------------------------------------

# if "x" not in st.session_state:
#     st.session_state.x = None
#     st.session_state.y = None
#     st.session_state.true_slope = None
#     st.session_state.true_intercept = None

# if "theta0" not in st.session_state:
#     st.session_state.theta0 = 1.00

# if "theta1" not in st.session_state:
#     st.session_state.theta1 = 0.00

# # ---------------------------------------------------------
# # Sidebar
# # ---------------------------------------------------------
# st.sidebar.title("Controls")

# num_points = st.sidebar.number_input(
#     "Number of Points",
#     min_value=5,
#     max_value=500,
#     value=30,
#     step=5
# )

# if st.sidebar.button("Generate Random Dataset"):

#     np.random.seed()

#     x = np.sort(np.random.uniform(0, 10, num_points))

#     true_slope = np.random.uniform(0.5, 3.5)
#     true_intercept = np.random.uniform(-2, 4)

#     noise = np.random.normal(0, 1, num_points)

#     y = true_slope * x + true_intercept + noise

#     st.session_state.x = x
#     st.session_state.y = y

#     st.session_state.true_slope = true_slope
#     st.session_state.true_intercept = true_intercept
    
#     st.session_state.theta0 = 1.00
#     st.session_state.theta1 = 0.00


# # =========================================================
# # θ0 Controls
# # =========================================================

# st.sidebar.markdown("### Slope (θ₀)")

# c1, c2, c3 = st.sidebar.columns([1,6,1])

# with c1:
#     if st.button("−", key="theta0_minus"):
#         st.session_state.theta0 = round(max(-10.0, st.session_state.theta0-0.01),2)

# with c3:
#     if st.button("+", key="theta0_plus"):
#         st.session_state.theta0 = round(min(10.0, st.session_state.theta0+0.01),2)

# theta0 = c2.number_input(
#     "",
#     min_value=-10.0,
#     max_value=10.0,
#     value=st.session_state.theta0,
#     step=0.01,
#     key="theta0_input"
# )

# theta0 = c2.slider(
#     "",
#     -10.0,
#     10.0,
#     theta0,
#     step=0.01,
#     key="theta0_slider"
# )

# st.session_state.theta0 = theta0


# # =========================================================
# # θ1 Controls
# # =========================================================

# st.sidebar.markdown("### Intercept (θ₁)")

# c1, c2, c3 = st.sidebar.columns([1,6,1])

# with c1:
#     if st.button("−", key="theta1_minus"):
#         st.session_state.theta1 = round(max(-10.0, st.session_state.theta1-0.01),2)

# with c3:
#     if st.button("+", key="theta1_plus"):
#         st.session_state.theta1 = round(min(10.0, st.session_state.theta1+0.01),2)

# theta1 = c2.number_input(
#     "",
#     min_value=-10.0,
#     max_value=10.0,
#     value=st.session_state.theta1,
#     step=0.01,
#     key="theta1_input"
# )

# theta1 = c2.slider(
#     "",
#     -10.0,
#     10.0,
#     theta1,
#     step=0.01,
#     key="theta1_slider"
# )

# st.session_state.theta1 = theta1

# theta0 = st.session_state.theta0
# theta1 = st.session_state.theta1


# # theta0 = st.sidebar.slider(
# #     "Slope (θ₀)",
# #     min_value=-10.0,
# #     max_value=10.0,
# #     value=1.0,
# #     step=0.1
# # )

# # theta1 = st.sidebar.slider(
# #     "Intercept (θ₁)",
# #     min_value=-10.0,
# #     max_value=10.0,
# #     value=0.0,
# #     step=0.1
# # )

# # ---------------------------------------------------------
# # Main Display
# # ---------------------------------------------------------
# if st.session_state.x is not None:

#     x = st.session_state.x
#     y = st.session_state.y

#     y_pred = theta0 * x + theta1

#     mse = np.mean((y - y_pred) ** 2)

#     col1, col2 = st.columns([3, 1])

#     # -----------------------------------------------------
#     # Plot
#     # -----------------------------------------------------
#     with col1:

#         fig, ax = plt.subplots(figsize=(7, 5))

#         ax.scatter(
#             x,
#             y,
#             color="royalblue",
#             s=50,
#             label="Observed Data"
#         )

#         ax.plot(
#             x,
#             y_pred,
#             color="crimson",
#             linewidth=3,
#             label="Regression Line"
#         )

#         ax.set_title("Linear Regression")

#         ax.set_xlabel("Independent Variable (x)")
#         ax.set_ylabel("Dependent Variable (y)")

#         ax.grid(True)

#         ax.legend()

#         st.pyplot(fig)

#     # -----------------------------------------------------
#     # Information Panel
#     # -----------------------------------------------------
#     with col2:

#         st.subheader("📊 Model Information")
#         st.markdown("### Prediction Equation")
#         st.latex(r"\hat{y}=\theta_0x+\theta_1")
#         st.markdown("### Current Regression Equation")

#         st.latex(
#             rf"\hat{{y}}={theta0:.2f}x+({theta1:.2f})"
#         )
#         # st.markdown("### Current Values")
#         # st.write(f"**Slope (θ₀):** {theta0:.2f}")
#         # st.write(f"**Intercept (θ₁):** {theta1:.2f}")
#         st.divider()
#         st.markdown("### Mean Squared Error")
#         st.metric(
#             label="Current MSE",
#             value=f"{mse:.4f}"
#         )
#         st.markdown("### MSE Formula")
#         st.latex(
#             r"\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2"
#         )
#         with st.expander("📖 Explanation"):
#             st.markdown(
#                 """
# **Where:**
# - **n** = Number of observations
# - **yᵢ** = Actual value
# - **ŷᵢ** = Predicted value
# - **(yᵢ − ŷᵢ)²** = Squared error
# The Mean Squared Error (MSE) measures the average squared
# difference between the observed and predicted values.
# - **Smaller MSE → Better Fit**
# - **Larger MSE → Poor Fit**
# """
#             )

#         st.divider()

#         if st.button("Reveal True Equation"):

#             st.success("Actual Equation Used to Generate the Dataset")

#             st.latex(
#                 rf"y={st.session_state.true_slope:.2f}x+{st.session_state.true_intercept:.2f}"
#             )

# else:

#     st.info("👈 Click **Generate Random Dataset** from the sidebar to begin.")



import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Linear Regression Visualizer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Linear Regression Visualizer")
st.write(
    """
This interactive application demonstrates how the **Slope (θ₀)** and
**Intercept (θ₁)** affect the regression line and the corresponding
**Mean Squared Error (MSE)**.

### Instructions
1. Select the number of random points.
2. Click **Generate Random Dataset**.
3. Adjust the sliders (or use the +/- buttons, or type a value manually) to fit the regression line.
4. Observe how the **MSE** changes.
5. Click **Reveal True Equation** to compare your estimate.
"""
)

# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------
if "x" not in st.session_state:
    st.session_state.x = None
    st.session_state.y = None
    st.session_state.true_slope = None
    st.session_state.true_intercept = None

if "xlim" not in st.session_state:
    st.session_state.xlim = None

if "ylim" not in st.session_state:
    st.session_state.ylim = None

# Canonical values for theta0 (slope) and theta1 (intercept)
if "theta0" not in st.session_state:
    st.session_state.theta0 = 1.0

if "theta1" not in st.session_state:
    st.session_state.theta1 = 0.0

STEP = 0.01
MIN_VAL = -10.0
MAX_VAL = 10.0

# ---------------------------------------------------------
# Callbacks to keep slider / manual input / +/- in sync
# ---------------------------------------------------------
def _sync_theta0_from_slider():
    st.session_state.theta0 = st.session_state.theta0_slider

def _sync_theta0_from_input():
    st.session_state.theta0 = st.session_state.theta0_input

def _increment_theta0():
    st.session_state.theta0 = round(
        min(MAX_VAL, st.session_state.theta0 + STEP), 2
    )

def _decrement_theta0():
    st.session_state.theta0 = round(
        max(MIN_VAL, st.session_state.theta0 - STEP), 2
    )

def _sync_theta1_from_slider():
    st.session_state.theta1 = st.session_state.theta1_slider

def _sync_theta1_from_input():
    st.session_state.theta1 = st.session_state.theta1_input

def _increment_theta1():
    st.session_state.theta1 = round(
        min(MAX_VAL, st.session_state.theta1 + STEP), 2
    )

def _decrement_theta1():
    st.session_state.theta1 = round(
        max(MIN_VAL, st.session_state.theta1 - STEP), 2
    )

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
st.sidebar.title("Controls")

num_points = st.sidebar.number_input(
    "Number of Points",
    min_value=5,
    max_value=500,
    value=30,
    step=5
)

if st.sidebar.button("Generate Random Dataset"):

    np.random.seed()

    x = np.sort(np.random.uniform(0, 10, num_points))

    true_slope = np.random.uniform(0.5, 3.5)
    true_intercept = np.random.uniform(-2, 4)

    noise = np.random.normal(0, 1, num_points)

    y = true_slope * x + true_intercept + noise

    st.session_state.x = x
    st.session_state.y = y

    # Store fixed axis limits
    x_margin = (x.max() - x.min()) * 0.05
    y_margin = (y.max() - y.min()) * 0.15
    
    st.session_state.xlim = (
        x.min() - x_margin,
        x.max() + x_margin
    )
    
    st.session_state.ylim = (
        y.min() - y_margin,
        y.max() + y_margin
    )

    st.session_state.true_slope = true_slope
    st.session_state.true_intercept = true_intercept

st.sidebar.divider()

# --- Ensure slider/input widgets reflect the canonical value before creation ---
st.session_state.theta0_slider = st.session_state.theta0
st.session_state.theta0_input = st.session_state.theta0

st.sidebar.markdown("**Slope (θ₀)**")
minus0, slider0, plus0 = st.sidebar.columns([1.2, 5.4, 1.4], vertical_alignment="bottom")
# minus0, slider0, plus0 = st.sidebar.columns([1, 6, 1])

with minus0:
    st.button("➖", key="theta0_minus_btn", on_click=_decrement_theta0)

with slider0:
    st.slider(
        "Slope (θ₀)",
        min_value=MIN_VAL,
        max_value=MAX_VAL,
        step=STEP,
        key="theta0_slider",
        on_change=_sync_theta0_from_slider,
        label_visibility="collapsed"
    )

with plus0:
    st.button("➕", key="theta0_plus_btn", on_click=_increment_theta0)

st.sidebar.number_input(
    "Enter θ₀ manually",
    min_value=MIN_VAL,
    max_value=MAX_VAL,
    step=STEP,
    key="theta0_input",
    on_change=_sync_theta0_from_input
)

st.sidebar.divider()

# --- Ensure slider/input widgets reflect the canonical value before creation ---
st.session_state.theta1_slider = st.session_state.theta1
st.session_state.theta1_input = st.session_state.theta1

st.sidebar.markdown("**Intercept (θ₁)**")
minus1, slider1, plus1 = st.sidebar.columns([1, 6, 1])

with minus1:
    st.button("➖", key="theta1_minus_btn", on_click=_decrement_theta1)

with slider1:
    st.slider(
        "Intercept (θ₁)",
        min_value=MIN_VAL,
        max_value=MAX_VAL,
        step=STEP,
        key="theta1_slider",
        on_change=_sync_theta1_from_slider,
        label_visibility="collapsed"
    )

with plus1:
    st.button("➕", key="theta1_plus_btn", on_click=_increment_theta1)

st.sidebar.number_input(
    "Enter θ₁ manually",
    min_value=MIN_VAL,
    max_value=MAX_VAL,
    step=STEP,
    key="theta1_input",
    on_change=_sync_theta1_from_input
)

theta0 = st.session_state.theta0
theta1 = st.session_state.theta1

# ---------------------------------------------------------
# Main Display
# ---------------------------------------------------------
if st.session_state.x is not None:

    x = st.session_state.x
    y = st.session_state.y

    y_pred = theta0 * x + theta1

    mse = np.mean((y - y_pred) ** 2)

    col1, col2 = st.columns([3, 1])

    # -----------------------------------------------------
    # Plot
    # -----------------------------------------------------
    with col1:

        fig, ax = plt.subplots(figsize=(7, 5))

        ax.scatter(
            x,
            y,
            color="royalblue",
            s=50,
            label="Observed Data"
        )

        ax.plot(
            x,
            y_pred,
            color="crimson",
            linewidth=3,
            label="Regression Line"
        )

        ax.set_title("Linear Regression")

        ax.set_xlabel("Independent Variable (x)")
        ax.set_ylabel("Dependent Variable (y)")

        # Keep axes fixed until a new dataset is generated
        ax.set_xlim(st.session_state.xlim)
        ax.set_ylim(st.session_state.ylim)

        ax.grid(True)

        ax.legend()

        st.pyplot(fig)

    # -----------------------------------------------------
    # Information Panel
    # -----------------------------------------------------
    with col2:

        st.subheader("📊 Model Information")
        st.markdown("### Prediction Equation")
        st.latex(r"\hat{y}=\theta_0x+\theta_1")
        st.markdown("### Current Values")
        st.latex(
            rf"\hat{{y}} = {theta0:.2f}x {'+' if theta1 >= 0 else '-'} {abs(theta1):.2f}"
        )
        st.divider()
        st.markdown("### Mean Squared Error")
        st.metric(
            label="Current MSE",
            value=f"{mse:.4f}"
        )
        st.markdown("### MSE Formula")
        st.latex(
            r"\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2"
        )
        with st.expander("📖 Explanation"):
            st.markdown(
                """
**Where:**
- **n** = Number of observations
- **yᵢ** = Actual value
- **ŷᵢ** = Predicted value
- **(yᵢ − ŷᵢ)²** = Squared error
The Mean Squared Error (MSE) measures the average squared
difference between the observed and predicted values.
- **Smaller MSE → Better Fit**
- **Larger MSE → Poor Fit**
"""
            )

        st.divider()

        if st.button("Reveal True Equation"):

            st.success("Actual Equation Used to Generate the Dataset")

            st.latex(
                rf"y={st.session_state.true_slope:.2f}x+{st.session_state.true_intercept:.2f}"
            )

else:

    st.info("👈 Click **Generate Random Dataset** from the sidebar to begin.")
