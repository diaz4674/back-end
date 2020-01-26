from random import randrange as rand




def gen_items():
    items = [
        {
            'model': 'piratestwo.item',
            'pk': 1,
            'fields': {
                'name': 'gold',
                'value': 1
            }
        },
        {
            'model': 'piratestwo.item',
            'pk': 2,
            'fields': {
                'name': 'gem',
                'value': 100
            }
        }
    ]
    return items

def gen_item_locations(map, num_of_items):
    items = []
    for n in range(num_of_items):
        while True:
            x = rand(len(map[0]))
            y = rand(len(map))
            if map[y][x] == 0: break
        item = gen_items()[rand(len(gen_items()))]
        items.append({
            'model': 'piratestwo.itemlocation',
            'pk': n,
            'fields': {
                'x': x,
                'y': y,
                'item_id': item['pk']
            }
        })
    return items

print(gen_item_locations(map_data['map'], 200),"call item gem")