# 📈 Linear Regression Visualizer

An interactive Streamlit application that demonstrates the fundamentals of **Linear Regression** by allowing users to manually adjust the regression line and observe how the **Mean Squared Error (MSE)** changes in real time.

The application is designed as a teaching and learning tool for students studying Machine Learning, Data Science, Artificial Intelligence, and Statistics.

---

## Features

- Generate random datasets with a user-defined number of points.
- Interactive control of:
  - **Slope (θ₀)**
  - **Intercept (θ₁)**
- Three methods to modify model parameters:
  - Slider
  - +/- buttons (0.01 step size)
  - Manual numeric input
- Live visualization of the regression line.
- Automatic calculation of Mean Squared Error (MSE).
- Displays the regression equation using the current parameter values.
- Displays the mathematical formula for MSE.
- Option to reveal the true equation used to generate the dataset.

## Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib

---

## Project Structure

```
Linear-Regression/
│
├── streamlit_app.py
├── requirements.txt
└── README.md/
```

---

## Educational Purpose

This project was developed as an interactive educational tool to help students visualize how Linear Regression works. Instead of only studying equations, users can interactively modify the slope and intercept of the regression line and immediately observe the resulting changes in the model fit and Mean Squared Error.

---

## License

This project is intended for educational purposes.
