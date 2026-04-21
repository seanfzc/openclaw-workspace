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
        # Note: pip install opendataloader-pdf might be needed if opendataloader is just a wrapper
        print(f"   You can try installing it using: pip install {library_name}")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred while checking '{library_name}': {e}")
        return False

def run_diagnostic():
    print("--- Python Environment Diagnostic Script ---")
    print("This script checks for the presence of 'opendataloader-pdf' and 'pymupdf4llm', and tesseract.\n")

    libs_found = True

    # Check for opendataloader-pdf
    if not check_library("opendataloader"): # Note: opendataloader itself is likely the import name
        libs_found = False

    print("-" * 20)

    # Check for pymupdf4llm
    if not check_library("pymupdf4llm"):
        libs_found = False

    print("-" * 20)

    # Check for tesseract
    try:
        print("Checking for tesseract...")
        result = subprocess.run(['command', '-v', 'tesseract'], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print(f"✅ Success: Tesseract found at: {result.stdout.strip()}")
        else:
            raise FileNotFoundError
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("❌ Error: Tesseract not found. Please ensure it is installed and in your PATH.")
        libs_found = False
    except Exception as e:
        print(f"❌ An unexpected error occurred while checking Tesseract: {e}")
        libs_found = False

    print("\n--- Diagnostic Summary ---")
    if libs_found:
        print("🚀 STATUS: ALL SYSTEMS GO")
        print("   All required components ('opendataloader', 'pymupdf4llm', 'tesseract') appear to be set up correctly.")
    else:
        print("❌ DEPENDENCY MISSING: Please review the errors above and install the missing components.")
    print("--------------------------")

if __name__ == "__main__":
    run_diagnostic()
