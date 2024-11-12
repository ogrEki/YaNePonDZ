result = []
def divider(a, b):
    if a < b:
      raise ValueError
    if b > 100:
      raise IndexError
    return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    try:
      res = divider(key, data[key])
      result.append(res)
    except ValueError:
        print(f"Помилка з ключем {key}: a ({key}) менше за b ({data[key]})")
    except IndexError:
        print(f"Помилка з ключем {key}: b ({data[key]}) більше за 100")
    except TypeError as e:
        print(f"Помилка з ключем {key}: {e}")
print(result)
