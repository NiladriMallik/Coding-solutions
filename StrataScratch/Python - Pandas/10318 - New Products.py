# Import your libraries
import pandas as pd

# Start writing code
# My solution
car_launches.head()
cars_merged = car_launches\
            .query("year == 2019")\
            .groupby(['year', 'company_name'])['product_name']\
            .count()\
            .reset_index(name = 'cars_2019')[['year', 'company_name', 'cars_2019']]\
            .merge(car_launches\
                    .query("year == 2020")\
                    .groupby(['year', 'company_name'])['product_name']\
                    .count()\
                    .reset_index(name = 'cars_2020'),
                    on = 'company_name', how = 'inner'
                )[['company_name', 'cars_2019', 'cars_2020']]
cars_merged['net_new_products'] = cars_merged['cars_2020'] - cars_merged['cars_2019']
cars_merged[['company_name', 'net_new_products']]

# Optimized solution by ChatGPT
cars_summary = (
    car_launches[car_launches['year'].isin([2019, 2020])]
    .groupby(['company_name', 'year'])['product_name']
    .count()
    .reset_index()
    .pivot(index='company_name', columns='year', values='product_name')
    .fillna(0)
    .astype(int)
    .rename(columns={2019: 'cars_2019', 2020: 'cars_2020'})
    .assign(net_new_products=lambda df: df['cars_2020'] - df['cars_2019'])
    .reset_index()[['company_name', 'net_new_products']]
)
