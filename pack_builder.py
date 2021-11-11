import json
import os

class Pack:
    _version_translation = {"1.16": 6, "1.15": 5, "1.14": 4}

    def __init__(self, pack_data):
        self.name = pack_data[0]
        self.namespace = pack_data[1]
        self.desc = pack_data[2]
        self.version = pack_data[3]
    
    def generate(self, path):
        pack_path = f"{path}/{self.name}/data/{self.namespace}"
        os.makedirs(f"{pack_path}/functions")

        pack_format = self._version_translation.get(self.version) if self._version_translation.get(self.version) != None else 0
        pack_meta = {"pack":{"pack_format": pack_format, "description":self.desc}}
        with open(f"{path}/{self.name}/pack.mcmeta", "w") as arc:
            arc.write(json.dumps(pack_meta, indent=1))