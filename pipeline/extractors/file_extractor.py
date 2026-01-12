from __future__ import annotations
from pipeline.extractors.interfaces import FileExtractor

import json
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Iterable, List, Dict, Any

import pandas as pd


class File_Extractor(FileExtractor):
    """
    data/
      *.zip          # outer archives
        *.zip        # inner archives
          *.json     # event files
    """

    def __init__(self, root: str | Path = "data"):
        self.root = Path(root)

    def _outer_archives(self) -> Iterable[Path]:
        # data/*.zip only
        return self.root.glob("*.zip")

    @staticmethod
    def _read_json_bytes(b: bytes) -> List[Dict[str, Any]]:
        if not b:
            return []
        
        text = b.decode("utf-8", errors="ignore").strip()
        if not text:
            return []
        
        events: List[Dict[str, Any]] = []

        try:
            obj = json.loads(text)
            if isinstance(obj, list):
                # проверяем, что все элементы — dict
                events = [item for item in obj if isinstance(item, dict)]
                if events:  # если хотя бы один dict
                    return events
        except json.JSONDecodeError:
            pass
        
        
        raise ValueError(f"err: {text[:200]}...")


    def _iter_events(self) -> Iterable[Dict[str, Any]]:
        for outer_path in self._outer_archives():
            with zipfile.ZipFile(outer_path) as outer_zip:
                # iterate inner *.zip in outer archive
                for inner_name in outer_zip.namelist():
                    if not inner_name.lower().endswith(".zip"):
                        continue

                    # read inner zip as bytes, then wrap in BytesIO
                    inner_bytes = outer_zip.read(inner_name)
                    with zipfile.ZipFile(BytesIO(inner_bytes)) as inner_zip:
                        # iterate *.json in inner archive
                        for json_name in inner_zip.namelist():
                            if not json_name.lower().endswith(".json"):
                                continue

                            raw = inner_zip.read(json_name)
                            for event in self._read_json_bytes(raw):
                                # Optional: attach provenance
                                event["_outer_zip"] = outer_path.name
                                event["_inner_zip"] = inner_name
                                event["_json_file"] = json_name
                                yield event


    def extract(self) -> pd.DataFrame:
        """
        Load all events into a single DataFrame.
        """
        events = list(self._iter_events())
        if not events:
            return pd.DataFrame()
        pd.DataFrame(events).to_csv('events_data.csv', index=False, sep=',', encoding='utf-8')
        return pd.DataFrame(events)
        

