# LNA Backend

## Local Development Setup

### Prerequisites

- Python 3.13 or higher
- Poetry (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd backend/lna-app
```

2. Install Poetry (if not already installed):
Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation) to install Poetry on your system.

3. Install dependencies:
```bash
poetry install
```

### Running the Application

1. Activate the poetry environment:
For details, see the [Poetry documentation on environment activation](https://python-poetry.org/docs/managing-environments/#bash-csh-zsh)

2. Start the development server:

**On macOS/Linux:**
```bash
uvicorn lna_app.main:app --reload
```

**On Windows:**
```bash
python -m uvicorn lna_app.main:app --reload
```

The application will be available at `http://localhost:8000`