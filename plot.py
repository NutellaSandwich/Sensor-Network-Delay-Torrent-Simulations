import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data = [(20, 3, 3),
(20, 9, 3),
(20, 15, 3),
(20, 21, 4),
(20, 27, 3),
(20, 33, 3),
(20, 39, 3),
(20, 45, 3),
(20, 51, 3),
(20, 57, 4),
(20, 63, 3),
(20, 69, 3),
(20, 75, 3),
(20, 81, 3),
(20, 87, 3),
(20, 93, 3),
(20, 99, 4),
(20, 105, 3),
(20, 111, 3),
(20, 117, 3),
(20, 123, 4),
(20, 129, 3),
(20, 135, 3),
(20, 141, 4),
(20, 147, 3),
(20, 153, 3),
(20, 159, 4),
(20, 165, 3),
(20, 171, 3),
(20, 177, 3),
(20, 183, 3),
(20, 189, 3),
(20, 195, 0),
(20, 201, 0),
(20, 207, 0),
(20, 213, 0),
(20, 219, 0),
(20, 225, 0),
(20, 231, 0),
(20, 237, 0),
(20, 243, 0),
(20, 249, 0),
(20, 255, 0),
(20, 261, 0),
(20, 267, 0),
(20, 273, 0),
(20, 279, 0),
(20, 285, 0),
(20, 291, 0),
(20, 297, 0),
(20, 303, 0),
(30, 3, 3),
(30, 9, 3),
(30, 15, 3),
(30, 21, 3),
(30, 27, 3),
(30, 33, 3),
(30, 39, 3),
(30, 45, 3),
(30, 51, 3),
(30, 57, 3),
(30, 63, 3),
(30, 69, 4),
(30, 75, 4),
(30, 81, 3),
(30, 87, 3),
(30, 93, 4),
(30, 99, 4),
(30, 105, 4),
(30, 111, 4),
(30, 117, 4),
(30, 123, 3),
(30, 129, 3),
(30, 135, 3),
(30, 141, 3),
(30, 147, 4),
(30, 153, 3),
(30, 159, 3),
(30, 165, 3),
(30, 171, 3),
(30, 177, 3),
(30, 183, 2),
(30, 189, 2),
(30, 195, 1),
(30, 201, 0),
(30, 207, 0),
(30, 213, 0),
(30, 219, 0),
(30, 225, 0),
(30, 231, 0),
(30, 237, 0),
(30, 243, 0),
(30, 249, 0),
(30, 255, 0),
(30, 261, 0),
(30, 267, 0),
(30, 273, 0),
(30, 279, 0),
(30, 285, 0),
(30, 291, 0),
(30, 297, 0),
(30, 303, 0),
(40, 3, 3),
(40, 9, 3),
(40, 15, 3),
(40, 21, 3),
(40, 27, 3),
(40, 33, 3),
(40, 39, 3),
(40, 45, 3),
(40, 51, 4),
(40, 57, 3),
(40, 63, 3),
(40, 69, 4),
(40, 75, 3),
(40, 81, 3),
(40, 87, 3),
(40, 93, 4),
(40, 99, 3),
(40, 105, 4),
(40, 111, 3),
(40, 117, 3),
(40, 123, 3),
(40, 129, 3),
(40, 135, 3),
(40, 141, 2),
(40, 147, 3),
(40, 153, 3),
(40, 159, 3),
(40, 165, 2),
(40, 171, 2),
(40, 177, 0),
(40, 183, 0),
(40, 189, 0),
(40, 195, 0),
(40, 201, 0),
(40, 207, 0),
(40, 213, 0),
(40, 219, 0),
(40, 225, 0),
(40, 231, 0),
(40, 237, 0),
(40, 243, 0),
(40, 249, 0),
(40, 255, 0),
(40, 261, 0),
(40, 267, 0),
(40, 273, 0),
(40, 279, 0),
(40, 285, 0),
(40, 291, 0),
(40, 297, 0),
(40, 303, 0),
(50, 3, 3),
(50, 9, 3),
(50, 15, 3),
(50, 21, 3),
(50, 27, 3),
(50, 33, 3),
(50, 39, 3),
(50, 45, 3),
(50, 51, 3),
(50, 57, 3),
(50, 63, 3),
(50, 69, 3),
(50, 75, 3),
(50, 81, 3),
(50, 87, 3),
(50, 93, 3),
(50, 99, 3),
(50, 105, 3),
(50, 111, 3),
(50, 117, 3),
(50, 123, 3),
(50, 129, 3),
(50, 135, 3),
(50, 141, 3),
(50, 147, 3),
(50, 153, 3),
(50, 159, 3),
(50, 165, 3),
(50, 171, 3),
(50, 177, 3),
(50, 183, 3),
(50, 189, 3),
(50, 195, 0),
(50, 201, 0),
(50, 207, 0),
(50, 213, 0),
(50, 219, 0),
(50, 225, 0),
(50, 231, 0),
(50, 237, 0),
(50, 243, 0),
(50, 249, 0),
(50, 255, 0),
(50, 261, 0),
(50, 267, 0),
(50, 273, 0),
(50, 279, 0),
(50, 285, 0),
(50, 291, 0),
(50, 297, 0),
(50, 303, 0),
(60, 3, 3),
(60, 9, 3),
(60, 15, 3),
(60, 21, 3),
(60, 27, 3),
(60, 33, 3),
(60, 39, 3),
(60, 45, 3),
(60, 51, 3),
(60, 57, 3),
(60, 63, 3),
(60, 69, 3),
(60, 75, 3),
(60, 81, 3),
(60, 87, 3),
(60, 93, 3),
(60, 99, 3),
(60, 105, 3),
(60, 111, 3),
(60, 117, 3),
(60, 123, 3),
(60, 129, 3),
(60, 135, 3),
(60, 141, 3),
(60, 147, 3),
(60, 153, 3),
(60, 159, 3),
(60, 165, 3),
(60, 171, 3),
(60, 177, 3),
(60, 183, 3),
(60, 189, 0),
(60, 195, 0),
(60, 201, 0),
(60, 207, 0),
(60, 213, 0),
(60, 219, 0),
(60, 225, 0),
(60, 231, 0),
(60, 237, 0),
(60, 243, 0),
(60, 249, 0),
(60, 255, 0),
(60, 261, 0),
(60, 267, 0),
(60, 273, 0),
(60, 279, 0),
(60, 285, 0),
(60, 291, 0),
(60, 297, 0),
(60, 303, 0),
(70, 3, 0),
(70, 9, 0),
(70, 15, 0),
(70, 21, 0),
(70, 27, 0),
(70, 33, 0),
(70, 39, 0),
(70, 45, 0),
(70, 51, 0),
(70, 57, 0),
(70, 63, 0),
(70, 69, 0),
(70, 75, 0),
(70, 81, 0),
(70, 87, 0),
(70, 93, 0),
(70, 99, 0),
(70, 105, 0),
(70, 111, 0),
(70, 117, 0),
(70, 123, 0),
(70, 129, 0),
(70, 135, 0),
(70, 141, 0),
(70, 147, 0),
(70, 153, 0),
(70, 159, 0),
(70, 165, 0),
(70, 171, 0),
(70, 177, 0),
(70, 183, 0),
(70, 189, 0),
(70, 195, 0),
(70, 201, 0),
(70, 207, 0),
(70, 213, 0),
(70, 219, 0),
(70, 225, 0),
(70, 231, 0),
(70, 237, 0),
(70, 243, 0),
(70, 249, 0),
(70, 255, 0),
(70, 261, 0),
(70, 267, 0),
(70, 273, 0),
(70, 279, 0),
(70, 285, 0),
(70, 291, 0),
(70, 297, 0),
(70, 303, 0),
(80, 3, 3),
(80, 9, 3),
(80, 15, 3),
(80, 21, 3),
(80, 27, 3),
(80, 33, 3),
(80, 39, 3),
(80, 45, 3),
(80, 51, 3),
(80, 57, 3),
(80, 63, 3),
(80, 69, 3),
(80, 75, 3),
(80, 81, 3),
(80, 87, 3),
(80, 93, 3),
(80, 99, 0),
(80, 105, 0),
(80, 111, 0),
(80, 117, 0),
(80, 123, 0),
(80, 129, 0),
(80, 135, 0),
(80, 141, 0),
(80, 147, 0),
(80, 153, 0),
(80, 159, 0),
(80, 165, 0),
(80, 171, 0),
(80, 177, 0),
(80, 183, 0),
(80, 189, 0),
(80, 195, 0),
(80, 201, 0),
(80, 207, 0),
(80, 213, 0),
(80, 219, 0),
(80, 225, 0),
(80, 231, 0),
(80, 237, 0),
(80, 243, 0),
(80, 249, 0),
(80, 255, 0),
(80, 261, 0),
(80, 267, 0),
(80, 273, 0),
(80, 279, 0),
(80, 285, 0),
(80, 291, 0),
(80, 297, 0),
(80, 303, 0),
(90, 3, 0),
(90, 9, 0),
(90, 15, 0),
(90, 21, 0),
(90, 27, 0),
(90, 33, 0),
(90, 39, 0),
(90, 45, 0),
(90, 51, 0),
(90, 57, 0),
(90, 63, 0),
(90, 69, 0),
(90, 75, 0),
(90, 81, 0),
(90, 87, 0),
(90, 93, 0),
(90, 99, 0),
(90, 105, 0),
(90, 111, 0),
(90, 117, 0),
(90, 123, 0),
(90, 129, 0),
(90, 135, 0),
(90, 141, 0),
(90, 147, 0),
(90, 153, 0),
(90, 159, 0),
(90, 165, 0),
(90, 171, 0),
(90, 177, 0),
(90, 183, 0),
(90, 189, 0),
(90, 195, 0),
(90, 201, 0),
(90, 207, 0),
(90, 213, 0),
(90, 219, 0),
(90, 225, 0),
(90, 231, 0),
(90, 237, 0),
(90, 243, 0),
(90, 249, 0),
(90, 255, 0),
(90, 261, 0),
(90, 267, 0),
(90, 273, 0),
(90, 279, 0),
(90, 285, 0),
(90, 291, 0),
(90, 297, 0),
(90, 303, 0),
(100, 3, 0),
(100, 9, 0),
(100, 15, 0),
(100, 21, 0),
(100, 27, 0),
(100, 33, 0),
(100, 39, 0),
(100, 45, 0),
(100, 51, 0),
(100, 57, 0),
(100, 63, 0),
(100, 69, 0),
(100, 75, 0),
(100, 81, 0),
(100, 87, 0),
(100, 93, 0),
(100, 99, 0),
(100, 105, 0),
(100, 111, 0),
(100, 117, 0),
(100, 123, 0),
(100, 129, 0),
(100, 135, 0),
(100, 141, 0),
(100, 147, 0),
(100, 153, 0),
(100, 159, 0),
(100, 165, 0),
(100, 171, 0),
(100, 177, 0),
(100, 183, 0),
(100, 189, 0),
(100, 195, 0),
(100, 201, 0),
(100, 207, 0),
(100, 213, 0),
(100, 219, 0),
(100, 225, 0),
(100, 231, 0),
(100, 237, 0),
(100, 243, 0),
(100, 249, 0),
(100, 255, 0),
(100, 261, 0),
(100, 267, 0),
(100, 273, 0),
(100, 279, 0),
(100, 285, 0),
(100, 291, 0),
(100, 297, 0),
(100, 303, 0),
(110, 3, 0),
(110, 9, 0),
(110, 15, 0),
(110, 21, 0),
(110, 27, 0),
(110, 33, 0),
(110, 39, 0),
(110, 45, 0),
(110, 51, 0),
(110, 57, 0),
(110, 63, 0),
(110, 69, 0),
(110, 75, 0),
(110, 81, 0),
(110, 87, 0),
(110, 93, 0),
(110, 99, 0),
(110, 105, 0),
(110, 111, 0),
(110, 117, 0),
(110, 123, 0),
(110, 129, 0),
(110, 135, 0),
(110, 141, 0),
(110, 147, 0),
(110, 153, 0),
(110, 159, 0),
(110, 165, 0),
(110, 171, 0),
(110, 177, 0),
(110, 183, 0),
(110, 189, 0),
(110, 195, 0),
(110, 201, 0),
(110, 207, 0),
(110, 213, 0),
(110, 219, 0),
(110, 225, 0),
(110, 231, 0),
(110, 237, 0),
(110, 243, 0),
(110, 249, 0),
(110, 255, 0),
(110, 261, 0),
(110, 267, 0),
(110, 273, 0),
(110, 279, 0),
(110, 285, 0),
(110, 291, 0),
(110, 297, 0),
(110, 303, 0),
(120, 3, 0),
(120, 9, 0),
(120, 15, 0),
(120, 21, 0),
(120, 27, 0),
(120, 33, 0),
(120, 39, 0),
(120, 45, 0),
(120, 51, 0),
(120, 57, 0),
(120, 63, 0),
(120, 69, 0),
(120, 75, 0),
(120, 81, 0),
(120, 87, 0),
(120, 93, 0),
(120, 99, 0),
(120, 105, 0),
(120, 111, 0),
(120, 117, 0),
(120, 123, 0),
(120, 129, 0),
(120, 135, 0),
(120, 141, 0),
(120, 147, 0),
(120, 153, 0),
(120, 159, 0),
(120, 165, 0),
(120, 171, 0),
(120, 177, 0),
(120, 183, 0),
(120, 189, 0),
(120, 195, 0),
(120, 201, 0),
(120, 207, 0),
(120, 213, 0),
(120, 219, 0),
(120, 225, 0),
(120, 231, 0),
(120, 237, 0),
(120, 243, 0),
(120, 249, 0),
(120, 255, 0),
(120, 261, 0),
(120, 267, 0),
(120, 273, 0),
(120, 279, 0),
(120, 285, 0),
(120, 291, 0),
(120, 297, 0),
(120, 303, 0),
(130, 3, 0),
(130, 9, 0),
(130, 15, 0),
(130, 21, 0),
(130, 27, 0),
(130, 33, 0),
(130, 39, 0),
(130, 45, 0),
(130, 51, 0),
(130, 57, 0),
(130, 63, 0),
(130, 69, 0),
(130, 75, 0),
(130, 81, 0),
(130, 87, 0),
(130, 93, 0),
(130, 99, 0),
(130, 105, 0),
(130, 111, 0),
(130, 117, 0),
(130, 123, 0),
(130, 129, 0),
(130, 135, 0),
(130, 141, 0),
(130, 147, 0),
(130, 153, 0),
(130, 159, 0),
(130, 165, 0),
(130, 171, 0),
(130, 177, 0),
(130, 183, 0),
(130, 189, 0),
(130, 195, 0),
(130, 201, 0),
(130, 207, 0),
(130, 213, 0),
(130, 219, 0),
(130, 225, 0),
(130, 231, 0),
(130, 237, 0),
(130, 243, 0),
(130, 249, 0),
(130, 255, 0),
(130, 261, 0),
(130, 267, 0),
(130, 273, 0),
(130, 279, 0),
(130, 285, 0),
(130, 291, 0),
(130, 297, 0),
(130, 303, 0),
(140, 3, 0),
(140, 9, 0),
(140, 15, 0),
(140, 21, 0),
(140, 27, 0),
(140, 33, 0),
(140, 39, 0),
(140, 45, 0),
(140, 51, 0),
(140, 57, 0),
(140, 63, 0),
(140, 69, 0),
(140, 75, 0),
(140, 81, 0),
(140, 87, 0),
(140, 93, 0),
(140, 99, 0),
(140, 105, 0),
(140, 111, 0),
(140, 117, 0),
(140, 123, 0),
(140, 129, 0),
(140, 135, 0),
(140, 141, 0),
(140, 147, 0),
(140, 153, 0),
(140, 159, 0),
(140, 165, 0),
(140, 171, 0),
(140, 177, 0),
(140, 183, 0),
(140, 189, 0),
(140, 195, 0),
(140, 201, 0),
(140, 207, 0),
(140, 213, 0),
(140, 219, 0),
(140, 225, 0),
(140, 231, 0),
(140, 237, 0),
(140, 243, 0),
(140, 249, 0),
(140, 255, 0),
(140, 261, 0),
(140, 267, 0),
(140, 273, 0),
(140, 279, 0),
(140, 285, 0),
(140, 291, 0),
(140, 297, 0),
(140, 303, 0),
(150, 3, 0),
(150, 9, 0),
(150, 15, 0),
(150, 21, 0),
(150, 27, 0),
(150, 33, 0),
(150, 39, 0),
(150, 45, 0),
(150, 51, 0),
(150, 57, 0),
(150, 63, 0),
(150, 69, 0),
(150, 75, 0),
(150, 81, 0),
(150, 87, 0),
(150, 93, 0),
(150, 99, 0),
(150, 105, 0),
(150, 111, 0),
(150, 117, 0),
(150, 123, 0),
(150, 129, 0),
(150, 135, 0),
(150, 141, 0),
(150, 147, 0),
(150, 153, 0),
(150, 159, 0),
(150, 165, 0),
(150, 171, 0),
(150, 177, 0),
(150, 183, 0),
(150, 189, 0),
(150, 195, 0),
(150, 201, 0),
(150, 207, 0),
(150, 213, 0),
(150, 219, 0),
(150, 225, 0),
(150, 231, 0),
(150, 237, 0),
(150, 243, 0),
(150, 249, 0),
(150, 255, 0),
(150, 261, 0),
(150, 267, 0),
(150, 273, 0),
(150, 279, 0),
(150, 285, 0),
(150, 291, 0),
(150, 297, 0),
(150, 303, 0),
(160, 3, 0),
(160, 9, 0),
(160, 15, 0),
(160, 21, 0),
(160, 27, 0),
(160, 33, 0),
(160, 39, 0),
(160, 45, 0),
(160, 51, 0),
(160, 57, 0),
(160, 63, 0),
(160, 69, 0),
(160, 75, 0),
(160, 81, 0),
(160, 87, 0),
(160, 93, 0),
(160, 99, 0),
(160, 105, 0),
(160, 111, 0),
(160, 117, 0),
(160, 123, 0),
(160, 129, 0),
(160, 135, 0),
(160, 141, 0),
(160, 147, 0),
(160, 153, 0),
(160, 159, 0),
(160, 165, 0),
(160, 171, 0),
(160, 177, 0),
(160, 183, 0),
(160, 189, 0),
(160, 195, 0),
(160, 201, 0),
(160, 207, 0),
(160, 213, 0),
(160, 219, 0),
(160, 225, 0),
(160, 231, 0),
(160, 237, 0),
(160, 243, 0),
(160, 249, 0),
(160, 255, 0),
(160, 261, 0),
(160, 267, 0),
(160, 273, 0),
(160, 279, 0),
(160, 285, 0),
(160, 291, 0),
(160, 297, 0),
(160, 303, 0),
(170, 3, 0),
(170, 9, 0),
(170, 15, 0),
(170, 21, 0),
(170, 27, 0),
(170, 33, 0),
(170, 39, 0),
(170, 45, 0),
(170, 51, 0),
(170, 57, 0),
(170, 63, 0),
(170, 69, 0),
(170, 75, 0),
(170, 81, 0),
(170, 87, 0),
(170, 93, 0),
(170, 99, 0),
(170, 105, 0),
(170, 111, 0),
(170, 117, 0),
(170, 123, 0),
(170, 129, 0),
(170, 135, 0),
(170, 141, 0),
(170, 147, 0),
(170, 153, 0),
(170, 159, 0),
(170, 165, 0),
(170, 171, 0),
(170, 177, 0),
(170, 183, 0),
(170, 189, 0),
(170, 195, 0),
(170, 201, 0),
(170, 207, 0),
(170, 213, 0),
(170, 219, 0),
(170, 225, 0),
(170, 231, 0),
(170, 237, 0),
(170, 243, 0),
(170, 249, 0),
(170, 255, 0),
(170, 261, 0),
(170, 267, 0),
(170, 273, 0),
(170, 279, 0),
(170, 285, 0),
(170, 291, 0),
(170, 297, 0),
(170, 303, 0),
(180, 3, 3),
(180, 9, 3),
(180, 15, 3),
(180, 21, 3),
(180, 27, 3),
(180, 33, 3),
(180, 39, 3),
(180, 45, 3),
(180, 51, 3),
(180, 57, 3),
(180, 63, 3),
(180, 69, 3),
(180, 75, 3),
(180, 81, 0),
(180, 87, 0),
(180, 93, 0),
(180, 99, 0),
(180, 105, 0),
(180, 111, 0),
(180, 117, 0),
(180, 123, 0),
(180, 129, 0),
(180, 135, 0),
(180, 141, 0),
(180, 147, 0),
(180, 153, 0),
(180, 159, 0),
(180, 165, 0),
(180, 171, 0),
(180, 177, 0),
(180, 183, 0),
(180, 189, 0),
(180, 195, 0),
(180, 201, 0),
(180, 207, 0),
(180, 213, 0),
(180, 219, 0),
(180, 225, 0),
(180, 231, 0),
(180, 237, 0),
(180, 243, 0),
(180, 249, 0),
(180, 255, 0),
(180, 261, 0),
(180, 267, 0),
(180, 273, 0),
(180, 279, 0),
(180, 285, 0),
(180, 291, 0),
(180, 297, 0),
(180, 303, 0),
(190, 3, 1),
(190, 9, 1),
(190, 15, 1),
(190, 21, 1),
(190, 27, 1),
(190, 33, 1),
(190, 39, 1),
(190, 45, 1),
(190, 51, 1),
(190, 57, 0),
(190, 63, 0),
(190, 69, 0),
(190, 75, 0),
(190, 81, 0),
(190, 87, 0),
(190, 93, 0),
(190, 99, 0),
(190, 105, 0),
(190, 111, 0),
(190, 117, 0),
(190, 123, 0),
(190, 129, 0),
(190, 135, 0),
(190, 141, 0),
(190, 147, 0),
(190, 153, 0),
(190, 159, 0),
(190, 165, 0),
(190, 171, 0),
(190, 177, 0),
(190, 183, 0),
(190, 189, 0),
(190, 195, 0),
(190, 201, 0),
(190, 207, 0),
(190, 213, 0),
(190, 219, 0),
(190, 225, 0),
(190, 231, 0),
(190, 237, 0),
(190, 243, 0),
(190, 249, 0),
(190, 255, 0),
(190, 261, 0),
(190, 267, 0),
(190, 273, 0),
(190, 279, 0),
(190, 285, 0),
(190, 291, 0),
(190, 297, 0),
(190, 303, 0),
(200, 3, 0),
(200, 9, 0),
(200, 15, 0),
(200, 21, 0),
(200, 27, 0),
(200, 33, 0),
(200, 39, 0),
(200, 45, 0),
(200, 51, 0),
(200, 57, 0),
(200, 63, 0),
(200, 69, 0),
(200, 75, 0),
(200, 81, 0),
(200, 87, 0),
(200, 93, 0),
(200, 99, 0),
(200, 105, 0),
(200, 111, 0),
(200, 117, 0),
(200, 123, 0),
(200, 129, 0),
(200, 135, 0),
(200, 141, 0),
(200, 147, 0),
(200, 153, 0),
(200, 159, 0),
(200, 165, 0),
(200, 171, 0),
(200, 177, 0),
(200, 183, 0),
(200, 189, 0),
(200, 195, 0),
(200, 201, 0),
(200, 207, 0),
(200, 213, 0),
(200, 219, 0),
(200, 225, 0),
(200, 231, 0),
(200, 237, 0),
(200, 243, 0),
(200, 249, 0),
(200, 255, 0),
(200, 261, 0),
(200, 267, 0),
(200, 273, 0),
(200, 279, 0),
(200, 285, 0),
(200, 291, 0),
(200, 297, 0),
(200, 303, 0),]

unique_speeds = set([item[0] for item in data])

# Create a 2D plot
plt.figure()

# Sort the unique speeds before plotting
sorted_unique_speeds = sorted(unique_speeds)

# Plot each speed in a different color, in sorted order
for speed in sorted_unique_speeds:
    x = [item[1] for item in data if item[0] == speed]
    y = [item[2] for item in data if item[0] == speed]
    plt.plot(x, y, marker='o', label=f'Speed {speed} m/s')

# Set labels for the axes
plt.xlabel('Distance (m)')
plt.ylabel('Readings')

# Add a legend
plt.legend()

# Show the plot
plt.show()