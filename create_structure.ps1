# Root folder
$root = "C:\Users\lenovo\Desktop\Copy-Mate-AI-Services-FolderSetup-FastAPI"

# Create directories
$dirs = @(
    ".github/workflows",
    "configs",
    "data/processed",
    "data/raw",
    "notebooks",
    "scripts",
    "src/api/v1",
    "src/db",
    "src/agents",
    "src/components",
    "src/pipeline",
    "tests"
)

foreach ($d in $dirs) { New-Item -ItemType Directory -Force -Path (Join-Path $root $d) }

# Create files
$files = @(
    ".github/workflows/main.yml",
    "configs/base.yaml",
    "configs/production.yaml",
    "notebooks/poc.ipynb",
    "scripts/data_ingestion.py",
    "scripts/evaluate_model.py",
    "src/__init__.py",
    "src/api/__init__.py",
    "src/api/main.py",
    "src/api/v1/__init__.py",
    "src/api/v1/endpoints.py",
    "src/api/v1/schemas.py",
    "src/db/__init__.py",
    "src/db/connection.py",
    "src/db/repository.py",
    "src/agents/__init__.py",
    "src/agents/planner.py",
    "src/components/__init__.py",
    "src/components/audio_processor.py",
    "src/components/web_scraper.py",
    "src/pipeline/__init__.py",
    "src/pipeline/prediction_pipeline.py",
    "src/prompts.py",
    "src/utils.py",
    "tests/__init__.py",
    "tests/test_api.py",
    "tests/test_pipeline.py",
    ".dockerignore",
    ".gitignore",
    ".env.local",
    ".env.staging",
    ".env.testing",
    ".env.production",
    "docker-compose.yml",
    "Dockerfile",
    "main.py",
    "pyproject.toml",
    "README.md"
)

foreach ($f in $files) { New-Item -ItemType File -Force -Path (Join-Path $root $f) }
