# 👁️ Computer Vision Exploration Sandbox

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.1%2B-green.svg)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-orange.svg)](https://numpy.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://pytest.org/)

A curated development sandbox designed for studying and implementing core computer vision algorithms, low-level image processing pipelines, and performance-optimized mathematical computations from first principles. 

This repository showcases clean engineering practices, test-driven development (TDD), and highly optimized array operations using **Python**, **OpenCV**, and **NumPy**.

---

## 🗺️ Project Directory Structure

```
computer-vision-sandbox/
├── 01_image_fundamentals/       # Foundational Image Processing
│   ├── src/
│   │   └── main.py             # Entry point executing the image pipeline
│   ├── utils/
│   │   ├── __init__.py         # Package initialization
│   │   └── functions.py        # Core image manipulation algorithms
│   └── test/
│       └── test.py             # Unit tests verifying implementations
├── 02_array_vectorization/      # High-Performance Array Filtering
│   ├── src/
│   │   ├── filters.py          # Naive, Vectorized, and Integral Box Filters
│   │   └── SmallVectorizationTutorial.ipynb
│   ├── test/
│   │   └── test_filters.py     # Unit tests verifying filter equivalence
│   └── README.md               # Exercise 2 Documentation & Takeaways
├── .gitignore                  # Git exclusion rules
└── README.md                   # Repository landing page (this file)
```

---

## ✨ Features & Implementations

### 1. Robust File I/O & Visualization
- Dynamic, side-by-side rendering of multiple images using OpenCV `imshow` and stalled window termination.
- Auto-directory creation during file writing to ensure robust batch-saving workflows without manual folder setup.

### 2. Precise Downscaling
- Half-size image scaling utilizing nearest-neighbor interpolation (`cv2.INTER_NEAREST_EXACT` on `cv2.resize`) for exact pixel preservation.

### 3. Channel Separation (Zero-Loop Vectorization)
- Separates BGR color images into three individual red, green, and blue visualization planes.
- Achieved using pure **NumPy slicing and multidimensional indexing** rather than slow nested loops, ensuring $\mathcal{O}(1)$ Python overhead:
```python
# Extract the blue channel in BGR color space
blue_plane = np.zeros_like(colored_image)
blue_plane[:, :, 0] = colored_image[:, :, 0]
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.6 or higher installed on your system.

### 2. Setup Virtual Environment & Install Dependencies
Navigate to the root directory and initialize the local development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/computer-vision-sandbox.git
cd computer-vision-sandbox

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install required packages
pip install opencv-python numpy pytest
```

---

## 💻 Running the Projects

### Running the Image Processing Pipeline
To execute the primary image processing demonstration which scales down an image, splits the BGR color channels, and saves the outputs:

```bash
python 01_image_fundamentals/src/main.py
```

*Outputs will be saved in `01_image_fundamentals/results/`.*

---

## 🧪 Testing

This project incorporates a robust suite of unit tests written in **Pytest** to ensure algorithmic correctness and mathematical consistency.

Run all tests in the workspace:
```bash
python -m pytest
```

---

## 🗺️ Modules & Takeaways

For detailed mathematical analysis, implementations, and core learnings of each module, check out their respective sub-READMEs:

1. **[01_image_fundamentals](file:///e:/Projects/computer_vision_sandbox/01_image_fundamentals)**: Core OpenCV visualization, BGR channel splitting, and nearest-neighbor resizing.
2. **[02_array_vectorization/README.md](file:///e:/Projects/computer_vision_sandbox/02_array_vectorization/README.md)**: Array slicing, performance profiling, and $\mathcal{O}(n^2)$ constant-time blurring via Integral Images.

---

## ⚡ Next Steps & Future Plans
- **Vectorized Spatial Filtering (Gaussian & Sharpening)**: Implement generalized spatial filters using NumPy stacking.
- **Edge Detection**: Custom Sobel operators and Canny Edge detection implementations.
