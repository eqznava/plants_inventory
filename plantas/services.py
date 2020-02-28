import csv
import os

from plantas.species import Plants

class PlantServices:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_plant(self, plant):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Plants.schema())
            writer.writerow(plant.to_dict())

    def list_plants(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Plants.schema())

            return list(reader)

    def update_plant(self, updated_plant):
        plants = self.list_plants()

        updated_plants = []
        for plant in plants:
            if plant['pui'] == updated_plant.pui:
                updated_plants.append(updated_plant.to_dict())
            else:
                updated_plants.append(plant)

        self._save_to_disk(updated_plants)

    def _save_to_disk(self, plants):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Plants.schema())
            writer.writerows(plants)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)

    def delete_plant(self, plant_pui):
        plants = self.list_plants()

        for plant in plants:
            if plant['pui'] == plant_pui.pui:
                plants.remove(plant)

        self._save_to_disk(plants)
