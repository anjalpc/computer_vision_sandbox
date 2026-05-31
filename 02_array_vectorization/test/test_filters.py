import pytest
import numpy as np
import os
import sys

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from filters import box_filter_loop, box_filter_vectorized, box_filter_integral

epsilon = 1e-5

def all_similar(img1: np.ndarray, img2: np.ndarray) -> bool:
    """Verifies that the difference between two arrays is within a small epsilon."""
    if img1.shape != img2.shape:
        return False
    max_diff = np.max(np.abs(img1 - img2))
    return max_diff < epsilon


def test_box_filter_vectorized():
    """Verifies that the vectorized slicing box filter matches the naive loop baseline."""
    # Generate a deterministic random image
    np.random.seed(42)
    img = (np.random.rand(100, 120) * 255).astype(np.float64)
    
    # Run both implementations
    naive_res = box_filter_loop(img, 5, 5)
    vectorized_res = box_filter_vectorized(img, 5, 5)
    
    assert all_similar(naive_res, vectorized_res), "Vectorized result does not match naive loop!"


def test_box_filter_integral():
    """Verifies that the integral image box filter matches the naive loop baseline."""
    np.random.seed(42)
    img = (np.random.rand(100, 120) * 255).astype(np.float64)
    
    # Run both implementations
    naive_res = box_filter_loop(img, 5, 5)
    integral_res = box_filter_integral(img, 5, 5)
    
    assert all_similar(naive_res, integral_res), "Integral image result does not match naive loop!"


def test_uneven_dimensions():
    """Verifies correctness with non-square filters (e.g. 3x7)."""
    np.random.seed(24)
    img = (np.random.rand(80, 90) * 255).astype(np.float64)
    
    naive_res = box_filter_loop(img, 7, 3)
    vectorized_res = box_filter_vectorized(img, 7, 3)
    integral_res = box_filter_integral(img, 7, 3)
    
    assert all_similar(naive_res, vectorized_res), "Vectorized result fails on uneven dimensions!"
    assert all_similar(naive_res, integral_res), "Integral result fails on uneven dimensions!"
