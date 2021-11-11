import json
import os

class Pack:
    def __init__(self, pack_data):
        self.name = pack_data[0]
        self.namespace = pack_data[1]
        self.desc = pack_data[2]
        self.version = pack_data[3]
    
    def generate(self, path):
        os.makedirs(f"{path}/{self.name}/data/minecraft/tags/functions")

        pack_path = f"{path}/{self.name}/data/{self.namespace}"
        os.makedirs(f"{pack_path}/functions")
        os.mkdir(f"{pack_path}/tags")
        os.mkdir(f"{pack_path}/tags/blocks")
        os.mkdir(f"{pack_path}/tags/items")
        os.mkdir(f"{pack_path}/tags/entity_types")
        os.mkdir(f"{pack_path}/advancements")
        os.mkdir(f"{pack_path}/predicates")
        os.mkdir(f"{pack_path}/loot_tables")
        os.mkdir(f"{pack_path}/recipes")

        pack_meta = {"pack":{"pack_format": self.version, "description":self.desc}}
        with open(f"{path}/{self.name}/pack.mcmeta", "w") as arc:
            arc.write(json.dumps(pack_meta, indent=1))
        
        # generate and config of tick and load functions
        load_config = {"values": [f"{self.namespace}:init"]}
        tick_config = {"values": [f"{self.namespace}:loop"]}
        with open(f"{path}/{self.name}/data/minecraft/tags/functions/load.json", "w") as load:
            load.write(json.dumps(load_config, indent=1))
        with open(f"{path}/{self.name}/data/minecraft/tags/functions/tick.json", "w") as tick:
            tick.write(json.dumps(tick_config, indent=1))
        
        for func in ["init", "loop"]:
            with open(f"{pack_path}/functions/{func}.mcfunction", "w") as arc:
                pass