---

# Continuous Integration Study

A simple project demonstrating continuous integration using GitHub Actions and a Streamlit-based calculator app. The repository explores the fundamentals of CI, automated testing with pytest, and GitHub Actions workflows.

---

## 🚀 Quick Overview

* **Goal**: Learn and experiment with continuous integration by creating a small Python project with tests and setting up a CI pipeline via GitHub Actions.
* **Pipeline / Workflow Steps**:

  * Write a [Streamlit app](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/app.py) that calculates the square, cube and fifth power of a user-provided integer.
  * Define corresponding pure Python functions (`square`, `cube`, `fifth_power`) and write [pytest tests](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/pytest_test.py) to validate them.
  * Configure a [GitHub Actions workflow](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.github/workflows/ci.yaml) to run on push or pull requests to the `main` branch and execute the tests.
* **Tech Stack**: Python, Streamlit, pytest, GitHub Actions.
* **Highlights**:

  * Minimal CI pipeline using YAML workflow to install dependencies and run tests.
  * Streamlit front-end for interactivity.
  * Basic pytest tests for mathematical functions.

---

## 📂 Repository Structure

| Path                                                                                                                            | Description                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [`.github/workflows/ci.yaml`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.github/workflows/ci.yaml) | GitHub Actions workflow that triggers on pushes and pull requests to `main`, sets up Python 3.9, installs dependencies and runs `pytest`. |
| [`app.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/app.py)                                       | Streamlit application where users input an integer and the app displays its square, cube and fifth power.                                 |
| [`pytest_test.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/pytest_test.py)                       | Contains simple functions (`square`, `cube`, `fifth_power`) and pytest tests that assert correct results and handle invalid input.        |
| [`requirements.txt`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/requirements.txt)                   | Lists Python dependencies (`streamlit`, `pytest`).                                                                                        |
| [`.gitignore`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.gitignore)                               | Standard Python `.gitignore` ignoring compiled files, virtual environments, caches and CI artifacts.                                      |
| [`LICENSE`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/LICENSE)                                     | MIT license for the project.                                                                                                              |

---

## ⚙️ How It Works

1. **Streamlit Calculator** – The [`app.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/app.py) file uses Streamlit to create a web UI with a number input widget. It calculates the square, cube and fifth power of the number at runtime.

2. **Test Functions** – [`pytest_test.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/pytest_test.py) defines pure functions (`square`, `cube`, `fifth_power`) and includes pytest test cases to verify correctness and invalid input handling.

3. **CI Workflow** – The [`.github/workflows/ci.yaml`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.github/workflows/ci.yaml) file defines a GitHub Actions pipeline that runs on push/pull requests to `main`. It checks out the repo, sets up Python 3.9, installs dependencies, and runs pytest.

---

## ▶️ Running the Project

### 1. Clone Repo

```bash
git clone https://github.com/PrakashD2003/Continuous-Integration-Study.git
cd Continuous-Integration-Study
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

This launches a local web interface where you can input a number and see its square, cube, and fifth power calculated live.

### 4. Run Tests Locally

```bash
pytest
```

### 5. CI Pipeline

When you push changes to `main` or open a pull request, GitHub Actions automatically runs the workflow in [`.github/workflows/ci.yaml`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.github/workflows/ci.yaml). It installs dependencies and runs the test suite.

---

## 📊 Key Learnings

* **Continuous Integration basics**: Automating tests with GitHub Actions.
* **Streamlit fundamentals**: Simple interactive web app.
* **Testing with pytest**: Unit tests, assertions, exception handling.
* **Workflow configuration**: YAML setup for GitHub Actions.

---

## 🔬 Detailed Breakdown (Optional)

### GitHub Actions Workflow

* Defined in [`.github/workflows/ci.yaml`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/.github/workflows/ci.yaml).
* Job: `build` → Runs on `ubuntu-latest`.
* Steps: checkout → setup Python 3.9 → install dependencies → run pytest.
* Triggers: push and pull requests to `main`.

### Streamlit App

* Implemented in [`app.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/app.py).
* Uses `st.number_input` to get input.
* Computes square, cube, fifth power → displays with `st.write`.

### Pytest Tests

* Implemented in [`pytest_test.py`](https://github.com/PrakashD2003/Continuous-Integration-Study/blob/main/pytest_test.py).
* Tests assert values for known inputs.
* Uses `pytest.raises` for invalid inputs.

---

## 🔮 Future Improvements

* Add more operations (e.g. square roots, factorials).
* Integrate code quality checks (flake8, black).
* Extend to Continuous Deployment (CD) by hosting the Streamlit app.
* Run CI matrix builds across Python versions/OS.
* Add coverage reporting (`coverage.py`).

---

## 🙌 Closing Notes

This project is a **concise example of setting up CI** for a Python application.
It highlights the synergy between **Streamlit (UI)**, **pytest (testing)**, and **GitHub Actions (automation)**.

👉 [View the Repository on GitHub](https://github.com/PrakashD2003/Continuous-Integration-Study)

---





























