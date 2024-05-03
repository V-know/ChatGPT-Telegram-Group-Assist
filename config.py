import logging
import yaml

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

fh = logging.FileHandler('main.log')

formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(fh)

# Load data from config.yaml file
with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
time_span = config["TIME_SPAN"]
token = config["MAX_TOKEN"]
context_count = config["CONTEXT_COUNT"]
rate_limit = config["RATE_LIMIT"]
notification_channel = config.get("NOTIFICATION_CHANNEL")
vip_groups = config.get("VIP_GROUPS")
