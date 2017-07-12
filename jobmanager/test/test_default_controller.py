# coding: utf-8

from __future__ import absolute_import

from jobmanager.models.job import Job
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_create_job(self):
        """
        Test case for create_job

        
        """
        body = Job()
        response = self.client.open('/api/job',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_job(self):
        """
        Test case for get_job

        
        """
        response = self.client.open('/api/job/{jobId}'.format(jobId='jobId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_job(self):
        """
        Test case for update_job

        
        """
        response = self.client.open('/api/job/{jobId}'.format(jobId='jobId_example'),
                                    method='PUT')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
