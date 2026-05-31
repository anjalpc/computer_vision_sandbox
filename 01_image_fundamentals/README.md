# 👁️ Exercise 1: Foundational Image Processing

A hands-on module introducing the fundamentals of image representation, file I/O operations, resizing, and vectorized channel extraction using **OpenCV** and **NumPy**.

---

## 🧠 Key Takeaways & Lessons Learned

### 1. Robust File I/O & Visualization
- Dynamic rendering of multiple images using OpenCV `imshow` and window management (`cv2.waitKey(0)`).
- Automatically creating target folders during file writing using `os.makedirs(folder, exist_ok=True)` to prevent file-write crashes if directories don't exist yet.

### 2. Precise Downscaling
- Half-size image scaling using nearest-neighbor interpolation (`cv2.INTER_NEAREST_EXACT` on `cv2.resize`) for exact pixel color preservation without artificial smoothing.

### 3. Channel Separation (Zero-Loop Vectorization)
- Separating a BGR color image into B, G, and R channels using pure **NumPy slicing**.
- Instead of using slow nested loops, we copy a single channel into a blank matrix of the same shape:
  ```python
  blue_plane = np.zeros_like(colored_image)
  blue_plane[:, :, 0] = colored_image[:, :, 0]
  ```
  This runs in $\mathcal{O}(1)$ Python interpreter overhead, which is much faster than running nested pixel loops.

---

## 🚀 Getting Started & Running the Code

### 1. Run the Image Processing Pipeline
To execute the pipeline which loads the camera image, downscales it, splits BGR channels, and saves the output images:
```bash
python src/main.py
```

### 2. Run the Automated Tests
Verify correctness of BGR channel summation, scaling, and robust file writing:
```bash
python -m pytest test/test_fundamentals.py
```
