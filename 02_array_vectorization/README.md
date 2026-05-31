# ⚡ Exercise 2: Array Vectorization & Integral Images

A development module designed to study the performance bottlenecks of pixel-by-pixel image processing in Python and implement high-performance, vectorized solutions using **NumPy** and **OpenCV**.

---

## 👁️ Core Objective: The Box Filter
The goal of this exercise is to implement a **Box Filter** (image blur) which replaces each pixel's value with the mathematical average of its neighborhood window. 

This folder explores three distinct stages of algorithmic optimization: from slow Python loops to instant matrix manipulations.

---

## 🧠 Key Takeaways & Lessons Learned

### 1. The Cost of Naive Loops
- **Implementation**: Slipping an $f \times f$ window over an $n \times n$ image using four nested loops.
- **Time Complexity**: $\mathcal{O}(f^2 \cdot n^2)$
- **Takeaway**: Doing pixel-by-pixel operations in Python is extremely slow because the interpreter must perform dynamic type-checking and execution overhead for every single pixel iteration.

### 2. Vectorization via Image Slicing
- **Implementation**: Instead of moving a window over the image, we shift the entire image by row/column offsets ($dy, dx$) inside the filter window.
- **Time Complexity**: $\mathcal{O}(f^2 \cdot n^2)$ theoretically, but execution is moved entirely to NumPy's compiled C-level backend.
- **Takeaway**: By slicing the array and adding whole matrix blocks together (`result += img[dy:dy+Rh, dx:dx+Rw]`), we eliminate loops over the large image dimensions entirely. The code runs **hundreds of times faster**.

### 3. Constant-Time Blurring with Integral Images
- **Implementation**: We precalculate a **Summed-Area Table** (Integral Image) where every coordinate $(y,x)$ contains the sum of all pixels above and to the left of it using `img.cumsum(axis=0).cumsum(axis=1)`.
- **Time Complexity**: $\mathcal{O}(n^2)$ — **completely independent of the blur size $f$!**
- **Takeaway**: Once the integral image is calculated, we can compute the sum of *any* sized rectangular window in constant time using only **4 corner lookups**:
  $$\text{Sum} = \text{TopLeft} + \text{BottomRight} - \text{TopRight} - \text{BottomLeft}$$
  Whether the blur window is $3 \times 3$ or $101 \times 101$, it runs at the exact same instant speed!

---

## 📊 Complexity & Performance Matrix

| Implementation | Time Complexity | Dtypes & Bounds | Performance |
| :--- | :--- | :--- | :--- |
| **Naive Loops** | $\mathcal{O}(f^2 \cdot n^2)$ | Python `float` / `int` | 🐌 **Very Slow** (Lags on small images) |
| **Vectorized Slicing** | $\mathcal{O}(f^2 \cdot n^2)$ | NumPy Vector Additions | ⚡ **Fast** (Bottlenecked by huge blurs) |
| **Integral Image** | $\mathcal{O}(n^2)$ | Constant-Time Lookup | 🚀 **Instant** (Constant speed for any blur size) |

---

## 🚀 Getting Started & Running the Code

### 1. Run the Visual Comparison Demo
Runs all three implementations on a test image from MIT and displays the result side-by-side using Matplotlib:
```bash
python src/filters.py
```

### 2. Run the Automated Tests
Run the `pytest` suite designed to verify correctness across multiple edge cases (uneven filters, non-square dimensions, etc.):
```bash
python -m pytest test/test_filters.py
```
