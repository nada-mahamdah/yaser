from logging import Logger

# from django.conf import settings
# from common.libs.harri_logger import Logger
import analytics as analytics

analytics.write_key = '8elno4cfk4'
def on_error(error, items):
    print("An error occurred with segment_io:", error)
    print(items)
    msg = 'An error occurred with segment_io:{error}, items:{items}'.format(error=error, items=str(items))
    Logger(__name__).extreme_logging(msg)
analytics.debug = True
analytics.on_error = on_error
class SegmentManager():
    # Register a new user to segment
    def __init__(self):
        pass
    def register(self, user_id, user_info):
        analytics.identify(user_id, user_info)

    def track(self, user_identifier, track_code, track_info=None):
        if track_info is None:
            track_info = {}
        print ("segmentttt>>>>>> TRACK::", user_identifier, track_code, track_info)
        analytics.track(user_identifier, track_code, track_info)