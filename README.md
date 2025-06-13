# NarrativeSync

NarrativeSync is an open-source toolkit for detecting and visualizing coordinated media narratives across news outlets and social media.

## Features
- Collects data from RSS feeds and social media
- Extracts and fingerprints key phrases using NLP
- Clusters and visualizes synchronized narratives
- Generates timeline charts and reports

## Installation
```bash
git clone https://github.com/YourOrg/NarrativeSync.git
cd NarrativeSync
pip install -r requirements.txt
```

## Usage
Edit `config.yaml` to add data sources, then run:
```bash
python run_sync.py
```

Results will be saved in the `output/` folder.

## License
MIT
