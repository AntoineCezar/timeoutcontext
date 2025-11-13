# Print help
help:
    just --list --unsorted

# Install / update the project's development virtualenv
install:
    uv sync --dev

[group('lint')]
check-all: check-python-formating check-python-typing check-python-docstrings check-toml-formating

# Check python formating
[group('lint')]
check-python-formating:
    uv run ruff check --select=F401,I001 src tests docs
    uv run ruff format --check src tests docs

# Check python typing
[group('lint')]
check-python-typing:
    uv run mypy --strict src
    uv run mypy tests

# Check python docstrings
[group('lint')]
check-python-docstrings:
    uv run pytest \
    	--ignore="./tests" \
    	--doctest-modules \

# Check toml formating
[group('lint')]
check-toml-formating:
    uv run tombi format --check

[group('lint')]
fix-all: fix-python-formating fix-toml-formating

# Fix python formating
[group('lint')]
fix-python-formating:
    uv run ruff check --fix --select=F401,I001 src tests docs
    uv run ruff format src tests docs

# Fix toml formating
[group('lint')]
fix-toml-formating:
    uv run tombi format

# Run tests
[group('test')]
test *ARGS:
    uv run pytest {{ ARGS }}

# Run and report code coverage
[group('test')]
coverage: coverage-run coverage-report

# Run code coverage measurement
[group('test')]
coverage-run *ARGS: clean-coverage
    uv run pytest --cov=timeoutcontext {{ ARGS }}

# Report code coverage
[group('test')]
coverage-report *ARGS="-m":
    uv run coverage report {{ ARGS }}

# Report code coverage in html
[group('test')]
coverage-report-html *ARGS:
    just coverage-report html {{ ARGS }}
    $(BROWSER) htmlcov/index.html

# Remove coverage artifacts
[group('test')]
clean-coverage:
    rm -f .coverage htmlcov/

# Build documentation
[group('build')]
build-docs: clean-docs
    mkdir -p docs/_static # Avoids missing dir warning
    make -C docs html SPHINXBUILD="uv run sphinx-build"
    echo "docs/_build/html/index.html"

# Remove docs build artifacts
[group('build')]
clean-docs:
    make -C docs clean SPHINXBUILD="uv run sphinx-build"

# Build package
[group('build')]
build-dist: clean-dist
    uv build 

# Remove package build artifacts
[group('build')]
clean-dist:
    rm -fr dist/
