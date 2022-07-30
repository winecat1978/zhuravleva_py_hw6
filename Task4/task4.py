# Все равны как на подбор
values = [0,2,4,6,10]
def same_by(characteristic,objects):
    return all(not characteristic(i) for i in objects)
if same_by(lambda x: x%2, values):
    print('same')
else:
    print('different')