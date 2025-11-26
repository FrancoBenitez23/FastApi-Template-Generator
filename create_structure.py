#!/usr/bin/env python3
"""
Script to create a FastAPI project structure with empty files and directories.
Includes a CLI to manage requirements.txt.
"""
import os
import sys
import subprocess
from pathlib import Path


def create_structure():
    """Create the complete directory and file structure inside app/ folder."""

    # Define the base directory
    base_dir = Path("app")

    # Define the structure as a list of paths (relative to app/)
    structure = [
        # Root files
        "__init__.py",
        "main.py",

        # API - Auth
        "api/auth/router.py",
        "api/auth/schemas.py",


        # API - Posts
        "api/posts/repository.py",
        "api/posts/router.py",
        "api/posts/schemas.py",


        # Core
        "core/db.py",
        "core/security.py",


        # Models
        "models/__init__.py",
    ]

    # Create base directory
    base_dir.mkdir(exist_ok=True)
    print(f"Created: {base_dir}/")

    # Create all directories and files inside app/
    for path in structure:
        file_path = base_dir / path

        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Create the file (empty)
        file_path.touch(exist_ok=True)
        print(f"Created: {file_path}")

    print("\n✓ Structure created successfully in app/ folder!")


def create_virtual_environment():
    """Create a virtual environment in the venv/ folder."""

    venv_path = Path("venv")

    if venv_path.exists():
        print(f"\n⚠ Virtual environment already exists at {venv_path}/")
        response = input("Do you want to recreate it? (y/n): ").strip().lower()
        if response != 'y':
            print("Keeping existing virtual environment.")
            return

    print("\n📦 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ Virtual environment created successfully in venv/ folder!")

        # Determine activation command based on OS
        if sys.platform == "win32":
            activate_cmd = "venv\\Scripts\\activate"
        else:
            activate_cmd = "source venv/bin/activate"

        print(f"\n💡 To activate the virtual environment, run:")
        print(f"  {activate_cmd}")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error creating virtual environment: {e}")
        sys.exit(1)


def manage_requirements():
    """Interactive CLI to manage requirements.txt and install dependencies."""

    requirements_file = Path("requirements.txt")
    packages = []

    # Load existing requirements if file exists
    if requirements_file.exists():
        with open(requirements_file, 'r') as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        if packages:
            print("\n📦 Current packages in requirements.txt:")
            for i, pkg in enumerate(packages, 1):
                print(f"  {i}. {pkg}")

    print("\n--- Requirements Manager ---")
    print("Add packages to requirements.txt (one per line)")
    print("Press Enter on empty line when done")
    print("Type 'skip' to skip this step\n")

    while True:
        package = input("Package name (with optional version, e.g., 'fastapi==0.104.1'): ").strip()

        if package.lower() == 'skip':
            print("Skipping requirements management.")
            return

        if not package:
            break

        if package not in packages:
            packages.append(package)
            print(f"  ✓ Added: {package}")
        else:
            print(f"  ⚠ Already in list: {package}")

    if not packages:
        print("\nNo packages to add.")
        return

    # Write requirements.txt
    with open(requirements_file, 'w') as f:
        f.write('\n'.join(packages) + '\n')

    print(f"\n✓ Created/Updated {requirements_file}")
    print(f"  Total packages: {len(packages)}")

    # Check if venv exists to provide appropriate next steps
    venv_path = Path("venv")
    if venv_path.exists():
        print("\n💡 Next steps:")
        if sys.platform == "win32":
            print("  1. Activate venv: venv\\Scripts\\activate")
        else:
            print("  1. Activate venv: source venv/bin/activate")
        print("  2. Install dependencies: pip install -r requirements.txt")
    else:
        print("\n💡 Next steps:")
        print("  1. Create a virtual environment: python -m venv venv")
        print("  2. Activate it: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)")
        print("  3. Install dependencies: pip install -r requirements.txt")


def main():
    """Main CLI menu."""

    while True:
        print("\n" + "=" * 50)
        print("  FastAPI Project Template Creator")
        print("=" * 50)

        print("\n1. Create project structure")
        print("2. Manage requirements.txt")
        print("3. Full setup (structure + venv + requirements)")
        print("4. Create virtual environment only")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            create_structure()
        elif choice == "2":
            manage_requirements()
        elif choice == "3":
            create_structure()
            create_virtual_environment()
            manage_requirements()
        elif choice == "4":
            create_virtual_environment()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\n❌ Invalid option. Please select 1-5.")


if __name__ == "__main__":
    main()