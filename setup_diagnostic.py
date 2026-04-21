import sys
import subprocess

def check_library(library_name):
    try:
        print(f"Checking for library: {library_name}")
        # Try to import the library
        __import__(library_name)
        print(f"✅ Success: '{library_name}' is importable.")
        return True
    except ImportError:
        print(f"❌ Error: '{library_name}' not found. Please ensure it is installed.")
        print(f"   You can try installing it using: pip install {library_name}")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred while checking '{library_name}': {e}")
        return False

def run_diagnostic():
    print("--- Python Environment Diagnostic Script ---")
    print("This script checks for the presence of 'opendataloader' and 'pymupdf4llm'.\n")

    libs_found = True

    # Check for opendataloader
    if not check_library("opendataloader"):
        libs_found = False

    print("-" * 20)

    # Check for pymupdf4llm
    if not check_library("pymupdf4llm"):
        libs_found = False

    print("\n--- Diagnostic Summary ---")
    if libs_found:
        print("✅ All required libraries ('opendataloader', 'pymupdf4llm') were found and are importable.")
        print("   Your Python environment appears to be set up correctly for these tools.")
    else:
        print("❌ Some required libraries were not found. Please review the errors above and install them.")
    print("--------------------------")

if __name__ == "__main__":
    run_diagnostic()
