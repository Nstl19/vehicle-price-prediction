import pandas as pd


FINAL_FEATURES = [
    'age_mileage',
    'transmission_type',
    'Max Power',
    'Max Torque',
    'engine_cc',
    'vehicle_age',
    'power_to_weight',
    'brand_name',
    'model_year',
    'seller_type_new',
    'mileage_new',
    'car_segment'
]


def prepare_input(
    model_year,
    transmission_type,
    engine_cc,
    max_power,
    max_torque,
    mileage,
    brand_name,
    seller_type,
    car_segment,
    km_driven,
    kerb_weight
):
    
    data = pd.DataFrame([{
        'model_year': model_year,
        'transmission_type': transmission_type,
        'engine_cc': engine_cc,
        'Max Power': max_power,
        'Max Torque': max_torque,
        'mileage_new': mileage,
        'brand_name': brand_name,
        'seller_type_new': seller_type,
        'car_segment': car_segment,
        'km_driven': km_driven,
        'Kerb Weight': kerb_weight
    }])

    # Feature engineering
    data['vehicle_age'] = 2026 - data['model_year']

    data['age_mileage'] = (
        data['vehicle_age'] * data['km_driven']
    )

    data['power_to_weight'] = (
        data['Max Power'] / data['Kerb Weight']
    )

    return data[FINAL_FEATURES]