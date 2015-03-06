import datetime
from dateutil import tz
from dateutil import parser
import channelcore as core
import bellstreams


###############################################

VIDEO_PREFIX = "/video/ctvnewsgo"
NAME = "CTV News Go"

ART = 'art-default.jpg'
ICON = 'icon-default.jpeg'

CHANNEL_LIST = [
	'https://raw.githubusercontent.com/pudds/JsonData/master/channels/ctvnews/ctvnews.json'
	]

###############################################

# This function is initially called by PMS to inialize the plugin
def Start():
	core.Init()
	

def GetScheduledShows(scheduleUrl):
	return bellstreams.GetScheduledShows(scheduleUrl)