import logging
import sys
import os
import traceback
import re

from app.Utilities.UtilRegex import UtilRegex

class UtilLog:
    Red='\033[0;31m'
    NoColor='\033[0m' # No Color

    ready = False
    LOGGER = None
    #this is called from app
    def initLog():
        if UtilLog.ready :
            return
        #only use gunicorn.error logger for all logging
        UtilLog.LOGGER = logging.getLogger('gunicorn.error')
        UtilLog.LOGGER.setLevel(os.environ.get('DEBUG_LEVEL','INFO'))
        UtilLog.LOGGER.debug('[UtilLog] initialized.')
        
        #sys.stderr = UtilLog
        sys.stdout = UtilLog

        UtilLog.ready = True

    def write(msg) :
        if not UtilLog.ready :
            UtilLog.initLog()
        if msg != "" and  msg != "\n":
            UtilLog.LOGGER.info('%s %s'%(UtilLog.get_caller(),msg))
    
    def flush():
        pass

    @staticmethod
    def info(msg, *args, **kwargs):
        if not UtilLog.ready :
            UtilLog.initLog()
        UtilLog.LOGGER.info('%s %s'%(UtilLog.get_caller(),msg))

    @staticmethod
    def debug(msg, *args, **kwargs):
        if not UtilLog.ready :
            UtilLog.initLog()
        UtilLog.LOGGER.debug('%s %s'%(UtilLog.get_caller(),msg))
        
    @staticmethod
    def error(msg, *args, **kwargs):
        if not UtilLog.ready :
            UtilLog.initLog()
        UtilLog.LOGGER.error('%s %s %s %s'%(UtilLog.Red,UtilLog.get_caller(),msg,UtilLog.NoColor))
    
    @staticmethod
    def get_caller():
        stack = traceback.format_stack()
        groups = UtilRegex.all_groups('\s+File\s+"(.*?)",\s+line\s+(\d+),\s+in\s+(.*?)\n',stack[-3])
        callerFile = re.sub('((.*?)\/)+(.*)\.py',r'\3',groups[0]) 
        callerLine = groups[1]
        callerFunc = groups[2]
        return '[%s.%s(%s)]'%(callerFile,callerFunc,callerLine)
