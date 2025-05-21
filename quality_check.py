import subprocess
import sys


def run_command(command, description):
    print(f"\n🔍 {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} passed.")
    except subprocess.CalledProcessError:
        print(f"❌ {description} failed.")
        sys.exit(1)


def main():
    # Run unit or functional test coverage
    run_command("pytest --cov=.", "Test coverage")

    # PEP8 compliance using pycodestyle
    run_command("pycodestyle . --exclude=venv,migrations,tests,quality_check.py,manage.py --max-line-length=100", "PEP8 compliance (pycodestyle)")

    # Lint using flake8
    # run_command("flake8 .", "Flake8 linting")
    run_command("flake8 . --exclude='.git,__pycache__,*/migrations/*,venv,quality_check.py' --max-line-length=100", "Flake8 linting compliance")

    # Security analysis with bandit
    run_command("bandit -r . --exclude '*/tests/*,*/venv/*,*/migrations/*,*quality_check.py*' --skip B101", "Bandit security analysis")

    # Type checking with mypy
    run_command("mypy . --exclude '(^|/)tests/|quality_check\.py|manage\.py|(^|/)venv/|(_test\.py$)' --ignore-missing-imports --disable-error-code var-annotated", "Python type annotations check (mypy)")

if __name__ == "__main__":
    main()
