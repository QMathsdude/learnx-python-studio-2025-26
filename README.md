# 🐍 LearnX+ Python Club 2025/26

[LOGO HERE]

## 🚀 About

This repository contains teaching materials for our weekly Python club meetings. We focus on building strong foundations in scientific computing libraries, suitable for members with beginner to intermediate Python experience.

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
- First of all, clone this repository. It should be named `learnx-python-club-2025-26`.

```bash
git clone https://github.com/QMathsdude/learnx-python-club-2025-26.git
```

- Next, create **new separate directory**. This will be linked to your **own remote repository**. 

```bash
mkdir DUPLICATE_DIR

git init # initialize git in directory
git remote add origin https://github.com/username/repo.git # link to your remote repository
```

### 2. Create & Update Conda Environment

- Change directory into `learnx-python-club-2025-26`.
```bash
cd learnx-python-club-2025-26
```

- If you do not have a Conda environment yet, create one using `environment.yml` (ensure you are within the same directory):

```bash
conda env create -f environment.yml
```

- Update Conda environment using `environment.yml` (ensure you are BOTH in the same directory, and the Conda environment is currently active within your terminal):

```bash
conda env update -f environment.yml --prune
```

### 3. Pull New Lessons

- Pull to get the latest week's lesson:
```bash
git fetch origin main
git merge origin/main 
```

- Check that the new learning material is indeed there.

### 4. Copy Locally & Push to Your Own Repository

- Copy the latest lesson into a separate directory (Bash, ZSH, Powershell):
```bash
cp -R ~/PATH/learnx-python-club-2025-26/Week_0X_TOPIC/ ~/PATH/DUPLICATE_DIR/
```

- After completing the lesson in the seperate directory, push to your own repository:
```bash
git status                  # check file status
git add .                   # add all files to staging area
git commit "Description"    # commit files in staging area
git status
git push                    # push to remote repository
```


## 📍 Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney
- [Scipy Lecture Notes](https://scipy-lectures.org/)

## ⚖️ License

The content of this project is dual-licensed.

*   **Code:** All Python scripts and code snippets are licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
*   **Educational Materials:** All other content, including PDF slides and recorded videos, are licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. See the [LICENSE.cc-by](LICENSE.cc-by) file for details.

---
