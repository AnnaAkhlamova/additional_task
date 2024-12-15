import pandas as pd
def get_average_rating():
    chocolate = pd.read_csv("flavors_of_cacao.csv", on_bad_lines="skip")
    average_ratings = chocolate.groupby('BeanType')['Rating'].mean().reset_index()
    while True:
        bean_type = input("Введіть тип бобів (наприклад, 'Criollo') або 'exit' для виходу: ").strip()
        if bean_type.lower() == 'exit':
            print("До побачення!")
            break
        matched = average_ratings[average_ratings['BeanType'].str.contains(bean_type, case=False, na=False)]
        if not matched.empty:
            print(f"Середня оцінка для типу бобів '{bean_type}': {matched['Rating'].values[0]:.2f}")
        else:
            print(f"Тип бобів '{bean_type}' не знайдений у даних.")

get_average_rating()
