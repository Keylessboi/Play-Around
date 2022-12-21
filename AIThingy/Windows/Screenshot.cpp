#include <Windows.h>
#include <iostream>

using namespace std;

// Function to take a screenshot and convert it to black and white
void screenshotToBW()
{
    // Get the screen dimensions
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);

    // Create a bitmap to hold the screenshot
    HBITMAP hBitmap = CreateCompatibleBitmap(GetDC(NULL), screenWidth, screenHeight);
    if (hBitmap == NULL)
    {
        cerr << "Unable to create bitmap" << endl;
        return;
    }

    // Create a device context to draw on the bitmap
    HDC hDC = CreateCompatibleDC(GetDC(NULL));
    if (hDC == NULL)
    {
        cerr << "Unable to create device context" << endl;
        return;
    }

    // Select the bitmap into the device context
    HBITMAP hOldBitmap = (HBITMAP)SelectObject(hDC, hBitmap);
    if (hOldBitmap == NULL)
    {
        cerr << "Unable to select bitmap" << endl;
        return;
    }

    // Capture the screen and draw it on the bitmap
    PrintWindow(GetDesktopWindow(), hDC, PW_CLIENTONLY);

    // Create a BITMAPINFO structure to hold the bitmap data
    BITMAPINFO bmi;
    ZeroMemory(&bmi, sizeof(bmi));
    bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
    bmi.bmiHeader.biWidth = screenWidth;
    bmi.bmiHeader.biHeight = -screenHeight;
    bmi.bmiHeader.biPlanes = 1;
    bmi.bmiHeader.biBitCount = 24;
    bmi.bmiHeader.biCompression = BI_RGB;

    // Allocate memory for the bitmap data
    BYTE* pBits = new BYTE[3 * screenWidth * screenHeight];
    if (pBits == NULL)
    {
        cerr << "Unable to allocate memory for bitmap data" << endl;
        return;
    }

    // Get the bitmap data
    GetDIBits(hDC, hBitmap, 0, screenHeight, pBits, &bmi, DIB_RGB_COLORS);

    // Convert the bitmap to grayscale
    for (int y = 0; y < screenHeight; y++)
    {
    }
}
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include "mylib.h"

namespace py = pybind11;
constexpr auto byref = py::return_value_policy::reference_internal;

PYBIND11_MODULE(MyLib, m) {
    m.doc() = "optional module docstring";

    py::class_<MyClass>(m, "MyClass")
    .def(py::init<double, double, int>())  
    .def("run", &MyClass::run, py::call_guard<py::gil_scoped_release>())
    .def_readonly("v_data", &MyClass::v_data, byref)
    .def_readonly("v_gamma", &MyClass::v_gamma, byref)
    ;
}