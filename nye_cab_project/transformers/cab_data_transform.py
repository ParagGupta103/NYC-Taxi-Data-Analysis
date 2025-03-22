import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df["request_datetime"] = pd.to_datetime(df["request_datetime"])
    df["on_scene_datetime"] = pd.to_datetime(df["on_scene_datetime"])
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"])

    df['shared_request_flag'] = df['shared_request_flag'].map({'Y': True, 'N': False}).astype('boolean')
    df['shared_match_flag'] = df['shared_match_flag'].map({'Y': True, 'N': False}).astype('boolean')
    df['access_a_ride_flag'] = df['access_a_ride_flag'].map({'Y': True, 'N': False}).astype('boolean')
    df['wav_request_flag'] = df['wav_request_flag'].map({'Y': True, 'N': False}).astype('boolean')
    df['wav_match_flag'] = df['wav_match_flag'].map({'Y': True, 'N': False}).astype('boolean')

    datetime_dim = df[['request_datetime','on_scene_datetime','dropoff_datetime','pickup_datetime']].drop_duplicates().reset_index(drop=True).copy()
    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim = datetime_dim[['datetime_id','request_datetime','dropoff_datetime','on_scene_datetime','pickup_datetime']]

    service_mapping = {
    'HV0002': 'Juno',
    'HV0003': 'Uber',
    'HV0004': 'Via',
    'HV0005': 'Lyft'
    }

    trip_dim = df[['PULocationID','DOLocationID','trip_miles','trip_time','hvfhs_license_num','dispatching_base_num','originating_base_num']].drop_duplicates().reset_index(drop=True).copy()
    trip_dim['trip_id'] = trip_dim.index
    trip_dim['service_name'] = trip_dim['hvfhs_license_num'].map(service_mapping)
    trip_dim = trip_dim[['trip_id','service_name','PULocationID','DOLocationID','trip_miles','trip_time','dispatching_base_num','originating_base_num','hvfhs_license_num']]

    flags_dim = df[['shared_request_flag','shared_match_flag','access_a_ride_flag','wav_request_flag','wav_match_flag']].drop_duplicates().reset_index(drop=True).copy()
    flags_dim['flag_id'] = flags_dim.index
    flags_dim = flags_dim[['flag_id','shared_request_flag','shared_match_flag','access_a_ride_flag','wav_request_flag','wav_match_flag']]
    
    fact_table = df.merge(
        datetime_dim, 
        on=['request_datetime', 'on_scene_datetime', 'pickup_datetime', 'dropoff_datetime']
    ).merge(
        trip_dim, 
        on=['PULocationID', 'DOLocationID', 'trip_miles', 'trip_time', 'hvfhs_license_num', 'dispatching_base_num', 'originating_base_num']
    ).merge(
        flags_dim, 
        on=['shared_request_flag', 'shared_match_flag', 'access_a_ride_flag', 'wav_request_flag', 'wav_match_flag']
    )[['datetime_id', 'trip_id', 'flag_id', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax', 'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay']]

    fact_table['vendor_id'] = fact_table.index
    new_column_order = [
        'vendor_id',          # Identifier
        'datetime_id',        # Foreign key for time
        'trip_id',            # Foreign key for trip details
        'flag_id',            # Foreign key for flags
        'base_passenger_fare', 
        'tolls', 
        'bcf', 
        'sales_tax', 
        'congestion_surcharge', 
        'airport_fee', 
        'tips', 
        'driver_pay'
    ]
    fact_table = fact_table[new_column_order]
    
    return {
        "datetime_dim":datetime_dim.to_dict(orient="dict"),
        "trip_dim":trip_dim.to_dict(orient="dict"),
        "flags_dim":flags_dim.to_dict(orient="dict"),
        "fact_table":fact_table.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
