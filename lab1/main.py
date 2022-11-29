import json

from Vehicles import Car, Gazelle, Kamaz, Truck, Belaz


def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))


car = Car(model='VW Polo', weight=1200, consumption=6, tank_capacity=45)
gazelle = Gazelle(model='Газель 3302', weight=1850, consumption=11, tank_capacity=70)
kamaz = Kamaz(model='Камаз 4310', weight=7080, consumption=30, tank_capacity=250)
truck = Truck(model='Scania s730', weight=8700, consumption=42, tank_capacity=500)
belaz = Belaz(model='БелАЗ-75710', weight=360000, height=8, consumption=1300, tank_capacity=5600)

objects = [car, gazelle, kamaz, truck, belaz, ]
data = {
        'vehicles': [],
}
for obj in objects:
    data['vehicles'].append(obj.__dict__)

write(data)
data.clear()
objects.clear()
data = read_from_json()
for obj in data['vehicles']:
    if obj['name'] == "Belaz":
        obj = Belaz(obj['model'], obj['weight'], obj['height'], obj['tank_capacity'], obj['consumption'])
    elif obj['name'] == "Car":
        obj = Car(obj['model'], obj['weight'], obj['tank_capacity'], obj['consumption'])
    elif obj['name'] == "Gazelle":
        obj = Gazelle(obj['model'], obj['weight'], obj['tank_capacity'], obj['consumption'])
    elif obj['name'] == "Kamaz":
        obj = Kamaz(obj['model'], obj['weight'], obj['tank_capacity'], obj['consumption'])
    elif obj['name'] == "Truck":
        obj = Truck(obj['model'], obj['weight'], obj['tank_capacity'], obj['consumption'])
    objects.append(obj)

with open(encoding='utf-8', file='output.txt', mode='w') as file:
    for obj in objects:
        output = obj.__repr__() + "\n"
        file.write(output)
