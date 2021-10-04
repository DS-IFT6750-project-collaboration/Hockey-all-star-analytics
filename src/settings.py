import dotenv
import os


project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)


# Local datafiles
data_folder = os.path.join(project_dir, 'data')
raw_data = os.path.join(data_folder, 'raw')
interim_data = os.path.join(data_folder, 'interim')
external_data = os.path.join(data_folder, 'external')
test_data = os.path.join(data_folder, 'test')
processed_data = os.path.join(data_folder, 'processed')
logg= os.path.join(project_dir, 'logs')



# Models
saved_models = os.path.join(project_dir, 'models')
