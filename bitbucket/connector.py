""" Copyright start
Copyright (C) 2008 - 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, _check_health

logger = get_logger('bitbucket')


class BitBucketConnector(Connector):
    def execute(self, config, operation, params, *args, **kwargs):
        try:
            operation_fn = operations.get(operation, 'custom')
            result = operation_fn(config, params, *args, **kwargs)
            return result
        except Exception as err:
            logger.error('An exception occurred {}'.format(err))
            raise ConnectorError('{}'.format(err))

    def check_health(self, config):
        try:
            return _check_health(config)
        except Exception as e:
            logger.exception("An exception occurred {}".format(e))
            raise ConnectorError(e)