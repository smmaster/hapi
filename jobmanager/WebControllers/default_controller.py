import connexion
from jobmanager.models.job import Job
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import redis
import uuid
import json
from  ..rmq import submit

def create_job(body=None):
    """
    create_job
    
    :param body: Job object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())
        #r = redis.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        id=str(uuid.uuid1())
        job={"id": "%s" % id,"status": "pending"}
        r.hset("jobs",id,json.dumps(job))
        submit(job)
    return job


def get_job(jobId):
    """
    get_job
    
    :param jobId: 
    :type jobId: str

    :rtype: Job
    """
    #r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)
    job=r.hget("jobs",jobId)
    if ( job):
        return json.loads(job)
    return connexion.NoContent,404


def update_job(jobId):
    """
    update_job
    
    :param jobId: 
    :type jobId: str

    :rtype: Job
    """
    return 'do some magic!'
