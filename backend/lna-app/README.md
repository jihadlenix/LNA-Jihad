# Lebanese News Aggregator (LNA)

A transparent news aggregation platform designed specifically for the Lebanese community. LNA collects, clusters, and presents news from multiple Lebanese news outlets in a unified, unbiased interface.

## Project Overview

peek into the [design doc](https://docs.google.com/document/d/1mQhErF_OxtlpF4VnKoWHPj01LEh_kh8je1mtFsdF8Qs/edit?tab=t.0#heading=h.kf5ih6ssd31o)

LNA aims to provide a single entry point for Lebanese news while maintaining complete transparency and neutrality. The system:
- Aggregates news from major Lebanese news outlets
- Clusters related articles into events to eliminate redundancy
- Generates descriptive titles and concise summaries for each event
- Presents original sources for every story, allowing readers to verify information
- Supports both English and Arabic content


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