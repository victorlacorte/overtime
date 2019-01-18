### TODO
* Maybe remove seconds (i.e. :00) from hours.timebank since it will never be
  utilized. For now we must call the ugly remove_seconds function

* The whole logic is non intuitive thanks to how datetime.timedelta functions
  with negative time. A solution would be to convert to seconds and then return
an appropriate object
