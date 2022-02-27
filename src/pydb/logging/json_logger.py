import logging
import json

class FormatterJSON(logging.Formatter):
    def format(self, record):
        record.message = record.getMessage()
        extra_data = record.__dict__.get('data')
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        j = {
            'levelname': record.levelname,
            'time': '%(asctime)s.%(msecs)dZ' % dict(asctime=record.asctime, msecs=record.msecs),
            'message': record.message,
            'module': record.module,
        }
        if extra_data is not None:
            j['extra_data'] = extra_data
        return json.dumps(j)

def get_logger(log_level):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel('INFO')

    formatter = FormatterJSON(
        '[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t%(levelno)s\t%(message)s\n',
        '%Y-%m-%dT%H:%M:%S'
    )
    # Replace the LambdaLoggerHandler formatter :
    logger.handlers[0].setFormatter(formatter)
    return logger