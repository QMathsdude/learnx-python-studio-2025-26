# 🐍 LearnX+ Python Studio 2025/26

![logo](./images/logo.png)

## 🚀 About

This repository contains teaching materials for our weekly Python meetings. We focus on building strong foundations in scientific computing libraries, suitable for members with beginner to intermediate Python experience.

## 🤖 Structure

Materials are organized by week/session:

```
Week_01_Conda/
├── README.md          # Topic overview
├── slides.pdf         # Presentation materials (if applicable)
├── lesson.ipynb       # Notes and exercises 
└── solution.ipynb     # Instructor's solution to lesson
```


## 📚 Topics 

A brief overview of the topics we cover is provided below. For more detailed information, please refer to [this PDF](topics-detailed.pdf), or the `README.md` file for each week.

![Aquirable Skills](./images/topics-covered.png)


## ⚙️ Getting Started

Below is the workflow for how the lessons will be conducted. Please follow closely.

![lesson-workflow](./images/lesson-workflow.gif)

### 1. Clone Repository & User Repository 
- First of all, clone this repository. It will be named `learnx-python-studio-2025-26`.

```bash
git clone https://github.com/QMathsdude/learnx-python-studio-2025-26.git
```

- Next, create **new separate directory** and change into it.

```bash
mkdir DUPLICATE_DIR  # make directory
cd DUPLICATE_DIR     # change directory
```

- Initialise Git locally in `DUPLICATE_DIR`. Then, link it to your **own remote repository**. 
```bash
git init                                                    # initialize git in directory
git remote add origin https://github.com/username/repo.git  # link to your remote repository
```

### 2. Pull New Lessons

- Change directory into `learnx-python-studio-2025-26`.
```bash
cd learnx-python-studio-2025-26
```

- Pull to get the latest week's lesson:
```bash
git fetch origin main
git merge origin/main 

ls  # list directory content
```

### 3. Copy Lessons Locally

- Copy the latest lesson into your personal directory `DUPLICATE_DIR` (Bash, ZSH, Powershell):
```bash
cp -R ~/PATH/learnx-python-studio-2025-26/Week_0X_TOPIC/ ~/PATH/DUPLICATE_DIR/
```

### 4. Push to Your Own Repository
- After completing the lesson in the seperate directory, push to your own repository:
```bash
git status                # check file status
git add .                 # add all files to staging area
git commit "Description"  # commit files in staging area
git status
git push                  # push to remote repository
```

### 5. Create & Update Conda Environment

- If you do not have a Conda environment yet, create one using `environment.yml` (ensure you are within the same directory as the YML file):

```bash
conda env create -f environment.yml
```

- Update Conda environment using `environment.yml` (ensure you are BOTH in the same directory and the Conda environment is currently active within your terminal):

```bash
conda env update -f environment.yml --prune
```


## 📍 Resources

- [Conda Documentation](https://docs.conda.io/en/latest/)
- [Jupyter Documentation](https://docs.jupyter.org/en/latest/)
- [ProGit Textbook](https://git-scm.com/book/en/v2)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [Learning Scientific Programming with Python (Christian Hill)](https://scipython.com/)


## ⚖️ License

The content of this project is dual-licensed.

*   **Code:** All Python scripts and code snippets are licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
*   **Educational Materials:** All other content, including PDF slides and recorded videos, are licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. See the [LICENSE.cc-by](LICENSE.cc-by) file for details.

---
