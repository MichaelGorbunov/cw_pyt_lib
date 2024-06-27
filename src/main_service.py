from src.data_conn import get_dataframe
from src.services import get_transfer_people

data_frame = get_dataframe()
print(get_transfer_people(data_frame))
