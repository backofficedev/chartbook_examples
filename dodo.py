"""Root dodo.py - Orchestrates builds across all pipelines and generates catalog docs for GitHub Pages."""

import shutil
from pathlib import Path

DOIT_CONFIG = {
    "backend": "sqlite3",
    "dep_file": "./.doit-db.sqlite",
    "num_process": 4,  # Run up to 4 tasks in parallel
}

BASE_DIR = Path(__file__).parent
CATALOG_DOCS = BASE_DIR / "catalog" / "docs"
ROOT_DOCS = BASE_DIR / "docs"


def copy_docs_action():
    """Copy catalog/docs to ./docs and add .nojekyll (module-level for pickling)"""
    # Remove existing docs if present
    if ROOT_DOCS.exists():
        shutil.rmtree(ROOT_DOCS)
    # Copy catalog/docs to root/docs
    shutil.copytree(CATALOG_DOCS, ROOT_DOCS)
    # Create .nojekyll file
    (ROOT_DOCS / ".nojekyll").touch()


def task_build_yield_curve():
    """Run doit in yield_curve directory"""
    return {
        "actions": ["doit -f ./yield_curve/dodo.py"],
        "file_dep": ["./yield_curve/dodo.py", "./yield_curve/chartbook.toml"],
        "targets": ["./yield_curve/docs/index.html"],
        "verbosity": 2,
    }


def task_build_fred_charts():
    """Run doit in fred_charts directory"""
    return {
        "actions": ["doit -f ./fred_charts/dodo.py"],
        "file_dep": ["./fred_charts/dodo.py", "./fred_charts/chartbook.toml"],
        "targets": ["./fred_charts/docs/index.html"],
        "verbosity": 2,
    }


def task_generate_catalog():
    """Run chartbook build in catalog directory"""
    return {
        "actions": ["cd catalog && chartbook build -f"],
        "file_dep": [
            "./catalog/chartbook.toml",
            "./yield_curve/docs/index.html",
            "./fred_charts/docs/index.html",
        ],
        "targets": ["./catalog/docs/index.html"],
        "task_dep": ["build_yield_curve", "build_fred_charts"],
        "verbosity": 2,
    }


def task_copy_docs():
    """Copy catalog/docs to ./docs and add .nojekyll"""
    return {
        "actions": [copy_docs_action],
        "file_dep": ["./catalog/docs/index.html"],
        "targets": ["./docs/index.html", "./docs/.nojekyll"],
        "task_dep": ["generate_catalog"],
        "verbosity": 2,
    }
