import importlib
import logging
import sys
from pathlib import Path

import kr8s

from icheck import ICheck
from prompt_toolkit import print_formatted_text as print

PLUGIN_DIR = Path(__file__).parent / "checks"


class K8Check:
    plugins: dict[str, ICheck] = {}
    client: kr8s.Api = None

    def __init__(self):
        self.load_plugins()
        self.check_k8s_connection()

    def load_plugins(self):
        for plugin in PLUGIN_DIR.glob("*.py"):
            try:
                if plugin.stem == "__init__":
                    continue
                plugin = importlib.import_module(f"checks.{plugin.stem}")
                for item in dir(plugin):
                    item = getattr(plugin, item)
                    if isinstance(item, type) and issubclass(item, ICheck) and item != ICheck:
                        check_classs: ICheck = item()
                        self.plugins[check_classs.name()] = check_classs
            except Exception as e:
                print(f"Error loading plugin {plugin.stem}")
                print(e)

        print(f"Loaded {len(self.plugins)} plugin(s):")
        for plugin in self.plugins:
            print(f" - {plugin}")

    def check_k8s_connection(self):
        try:
            self.client = kr8s.api()
        except Exception as e:
            print(f"Error connecting to k8s cluster")
            print(e)
            sys.exit(1)
        print(f"Connected to k8s cluster as {self.client.whoami()}")


if __name__ == "__main__":
    K8Check()
