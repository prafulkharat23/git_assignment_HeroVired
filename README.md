# Git Assignment – Hero Vired

This repository contains solutions to the Git assignment for Hero Vired. The project includes the following Python applications:

1. **CalculatorPlus**
2. **Git LFS Integration**
3. **Geometry Calculator**

---

## 📦 Repository Details

- **Name:** `git_assignment_HeroVired`  
- **URL:** [https://github.com/prafulkharat23/git_assignment_HeroVired](https://github.com/prafulkharat23/git_assignment_HeroVired)
- **Owner:** Yogeswaaran Panneerselvam (yogi9016)
- **Collaborator:** Praful Kharat (prafulkharat23)

---

## ✅ 1. CalculatorPlus

### 🚀 Setup & Branching

```bash
git checkout -b dev
git add calculator.py
git commit -m "Initial calculator app with square root function"
git push origin -u dev
```

### 🏷️ Release v1.0

```bash
git checkout main
git merge dev
git tag v1.0
git push origin main --tags
```

### 🌱 Feature Branch: square root

```bash
git checkout -b feature/sqrt
# Implement square root functionality
git commit -am "Feature: square root is complete"
git push origin -u feature/sqrt
```

### 🐞 Bug Fix: divide by zero (in dev)

```bash
# Fix divide() function in dev branch
# def divide(self, a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero.")
#     return a / b

# Then update feature/sqrt
git checkout feature/sqrt
git merge dev
git push origin feature/sqrt
```

### 🔃 Merge Feature → Dev → Main

```bash
git checkout dev
git merge feature/sqrt

# Test the code
python calculator.py

git checkout main
git merge dev
git tag v2.0
git push origin main --tags
```

---

## ✅ 2. Git LFS Integration

### 🔧 Setup Git LFS

```bash
brew install git-lfs     
git lfs install
git lfs track "*.bin"
```

> This creates or updates `.gitattributes`.

### 📂 Add 99MB Dummy File

```bash
dd if=/dev/urandom of=largefile.bin bs=1M count=99
git add .gitattributes bigfile.bin
git commit -m "Add dummy 250MB binary file for LFS testing"
git push origin -u lfs
```

---

## ✅ 3. Geometry Calculator

### 🔄 Create Base Branch

```bash
git checkout dev
git checkout -b geometry-calculator
```

### 📝 Create `geometry.py`

Add the following structure and test using:

```bash
python geometry.py
```

---

### 🔁 Feature Branch: Circle Area

```bash
git checkout -b feature/circle-area
# Begin coding but stash incomplete work
git stash save "WIP: circle_area"

# Later...
git stash list
git stash apply 0
git commit -am "circle_area is completed"
git push origin -u feature/circle-area
```

---

### 🔁 Feature Branch: Rectangle Area

```bash
git checkout -b feature/rectangle-area
# Apply stash for rectangle feature
git stash list
git stash apply 1
git commit -am "rectangle-area is completed"
git push origin -u feature/rectangle-area
```

---

## 🤝 Collaboration & Review

- Added **yogi9016** as a collaborator to the repository.
- Pull requests were created from both feature branches (`feature/circle-area` and `feature/rectangle-area`) to the `dev` branch.
- **yogi9016** reviewed and approved the pull requests.
- After successful testing, both features were merged into `main`.

---

## 🏁 Summary

- ✔️ CalculatorPlus v1.0 and v2.0 released  
- ✔️ Git LFS integrated with a 250MB file  
- ✔️ Geometry calculator completed using `git stash` and branching  
- ✔️ Code reviewed and approved by collaborator `yogi9016`